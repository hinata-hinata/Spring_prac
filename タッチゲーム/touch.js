"use strict";

const easy = document.getElementById('easy');
const container = document.getElementById('container');
const images = ['penginn.gif', 'sirokuma.gif', 'tokage.jpg', 'tonnkatu.gif'];
const img = document.createElement('img');
let current = 0;
let intervalId;

easy.addEventListener('click', function () {
  all_delete();
  intervalId = setInterval(main, 300);
  add_stop_button();
});

//すべての要素を削除
function all_delete() {
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
}

function main() {
  // const img = document.createElement('img');
  img.src = images[current];
  container.appendChild(img);
  current = (current + 1) % images.length;
}

function add_stop_button(){
  const StopBtn = document.createElement('button');
  StopBtn.textContent = 'STOP';
  StopBtn.classList.add('stopbtn');
  StopBtn.addEventListener('click', function(){
    clearInterval(intervalId);
  })
  container.appendChild(StopBtn);
}