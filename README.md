
## Ejecución

1. Inicia la aplicación:
    ```bash
    flask run
    ```

2. Abre tu navegador web y navega a `http://127.0.0.1:5000` para interactuar con la aplicación.

## Detalles de la Implementación

### `app.py`

Este archivo contiene la lógica principal de la aplicación. A continuación se describe brevemente cada ruta:

- `/`: Muestra la página principal.
- `/upload`: Permite a los usuarios subir una imagen.
- `/ask_test`: Muestra una pantalla intermedia antes del test.
- `/test`: Permite a los usuarios realizar el Test CARS.
- `/result`: Muestra el resultado del Test CARS y la predicción basada en la imagen subida.

### Plantillas HTML

- `upload.html`: Página para subir una imagen.
- `ask_test.html`: Página intermedia que se muestra después de subir una imagen.
- `test.html`: Página para realizar el Test CARS.
- `result.html`: Página que muestra el resultado del test.

### Archivos Estáticos

- `styles.css`: Contiene los estilos para las diferentes páginas de la aplicación.
- `scripts.js`: Contiene los scripts necesarios para la funcionalidad de la aplicación.

### Carpetas de Subidas

- `uploads/`: Esta carpeta almacena las imágenes que los usuarios suben a la aplicación.

## Notas Adicionales

- Asegúrate de tener un modelo predictivo entrenado y disponible si deseas utilizar la funcionalidad de predicción basada en imágenes.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, realiza un fork del proyecto y envía un pull request con tus cambios.


   Documento creado y mantenido por Maximo Ocaña
   
   Fecha: 07/2024
   
   Propósito: Este documento forma parte de un proyecto web.
   
   Descripción: V1 TEA detection. 

