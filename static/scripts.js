
//    Documento creado y mantenido por Maximo Ocaña
//    Fecha: 07/2024
//    Propósito: Este documento forma parte de un proyecto web.
//    Descripción: V1 TEA detection.

document.getElementById('fileInput').addEventListener('change', function(event) {
    const preview = document.getElementById('previewImage');
    const file = event.target.files[0];
    const reader = new FileReader();
  
    reader.onloadend = function() {
      preview.src = reader.result;
      document.getElementById('continueButton').style.display = 'block';
    };
  
    if (file) {
      reader.readAsDataURL(file);
    } else {
      preview.src = '';
      document.getElementById('continueButton').style.display = 'none';
    }
  });


//content  
const startButton = document.getElementById('startButton');
const modal = document.getElementById('uploadModal');
const closeModal = document.getElementsByClassName('close')[0];
const fileInput = document.getElementById('fileInput');
const previewImage = document.getElementById('previewImage');
const continueButton = document.getElementById('continueButton');

startButton.addEventListener('click', () => {
  modal.style.display = 'flex';
});

closeModal.addEventListener('click', () => {
  modal.style.display = 'none';
});

window.addEventListener('click', (event) => {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
});

// Animación del botón al hacer hover
startButton.addEventListener('mouseover', () => {
  startButton.style.transform = 'scale(1.1)';
});

startButton.addEventListener('mouseout', () => {
  startButton.style.transform = 'scale(1)';
});

// Manejo del cambio en el input de archivo
fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      previewImage.src = e.target.result;
      previewImage.style.display = 'block';
      continueButton.style.display = 'block';
    };
    reader.readAsDataURL(file);
  }
});

continueButton.addEventListener('click', () => {
  // Lógica para redirigir a otra página
  window.location.href = 'siguiente_pagina.html';
});

