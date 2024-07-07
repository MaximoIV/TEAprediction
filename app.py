
#   Documento creado y mantenido por Maximo Ocaña
#   Fecha: 07/2024
#   Propósito: Este documento forma parte de un proyecto web.
#   Descripción: V1 TEA detection.


from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
app.secret_key = 'changePassword'

# Configuraciones
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Cargar el modelo
model_path = 'uploadYourModelexample:"model\predictive_model.h5'
model = load_model(model_path)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Redimensionar la imagen a 224x224
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    # Usar np.argmax para obtener la predicción
    predicted_class = np.argmax(prediction, axis=1)[0]
    return 1 if predicted_class > 0.5 else 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files or 'terms' not in request.form:
            return redirect(url_for('thanks'))
        
        file = request.files['file']
        if file.filename == '':
            return redirect(url_for('thanks'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Realizar la predicción
            prediction = predict_image(file_path)
            
            # Almacenar la predicción en la sesión
            session['image_prediction'] = prediction
            
            return redirect(url_for('ask_test'))
    return render_template('upload.html')

@app.route('/ask_test', methods=['GET', 'POST'])
def ask_test():
    if request.method == 'POST':
        consent = request.form.get('consent')
        if consent == 'no':
            return redirect(url_for('thanks'))
        elif consent == 'yes':
            return redirect(url_for('test'))
    return render_template('ask_test.html')

@app.route('/test', methods=['GET', 'POST'])
def test():

     # Recoger las respuestas del test CARS
      # score{i} = float(request.form['score{i}']) if 'score{i}' in request.form else 0
    if request.method == 'POST':
        num_questions = 15
        points = 0
        for i in range(1, num_questions + 1):
            key = f'score{i}'
            if key in request.form:
                points += float(request.form[key])
       
        scores = request.form.getlist('score')
        total_scores = sum(map(int, scores))
        total_score = points + total_scores

        
        if total_score < 30:
            test_result = 'ausencia de autismo'
        elif 30 <= total_score < 36:
            test_result = 'autismo moderado'
        else:
            test_result = 'autismo severo'

        image_prediction = session.get('image_prediction', 0)
        
        # Determinar el mensaje final
        if test_result == 'autismo moderado':
            if image_prediction == 0:
                message = 'Su hijo supuestamente tiene autismo moderado.'
            else:
                message = 'Su hijo tiene autismo moderado.'
        elif test_result == 'autismo severo':
            if image_prediction == 0:
                message = 'Su hijo supuestamente tiene autismo severo.'
            else:
                message = 'Su hijo tiene autismo severo.'
        else:  # ausencia de autismo
            if image_prediction == 0:
                message = 'Su hijo tiene ausencia de autismo.'
            else:
                message = 'Su hijo supuestamente tiene ausencia de autismo.'

        return render_template('result.html', result=message)
    
    return render_template('test.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(debug=True)
