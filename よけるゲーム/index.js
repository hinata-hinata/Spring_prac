"use strict";

const easy = document.getElementById('easy');
const container = document.getElementById('container');

// const canvas = document.getElementById('myCanvas');
// const ctx = canvas.getContext('2d');

const canvas = document.createElement('canvas');
canvas.width = 400; // 幅を設定
canvas.height = 600; // 高さを設定
// canvas.id = 'newCanvas'; 
const ctx = canvas.getContext('2d');


let x1 = Math.floor(Math.random() * 380 + 20);
let y1 = 0;
let x2 = Math.floor(Math.random() * 380 + 20);
let y2 = 0;
const radius = 20;

let rectX = 150;
const rectY = 500;
const rectWidth = 100;
const rectHeight = 20;
const rectSpeed = 20;

easy.addEventListener('click', function(){
  all_delete();
  draw()
})

function all_delete(){
  while(container.firstChild){
    container.removeChild(container.firstChild);
  }
}

function draw() {
  container.appendChild(canvas);
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  ctx.beginPath();
  ctx.arc(x1, y1, radius, 0, Math.PI * 2);
  ctx.fillStyle = 'green';
  ctx.fill();

  ctx.fillStyle = 'red';
  ctx.fillRect(rectX, rectY, rectWidth, rectHeight);

  y1 += 6;

  ctx.beginPath();
  ctx.arc(x2, y2, radius, 0, Math.PI * 2);
  ctx.fillStyle = 'blue';
  ctx.fill();

  y2 += 8;

  if (y1 + radius >= rectY && x1 >= rectX && x1 <= rectX + rectWidth) {
    location.reload();
  }

  if (y2 + radius >= rectY && x2 >= rectX && x2 <= rectX + rectWidth) {
    location.reload();
  }

  if (y1 + radius > canvas.height) {
    y1 = 0; // 円を上にリセット
    x1 = Math.floor(Math.random() * 380 + 10);
  }

  if (y2 + radius > canvas.height) {
    y2 = 0; // 円を上にリセット
    x2 = Math.floor(Math.random() * 380 + 10);
  }

  requestAnimationFrame(draw);
}

function handleKeyDown(event) {
  if (event.key === 'ArrowLeft') {
    rectX = Math.max(rectX - rectSpeed, 0); // 左に移動
  } else if (event.key === 'ArrowRight') {
    rectX = Math.min(rectX + rectSpeed, canvas.width - rectWidth); // 右に移動
  }
}

document.addEventListener('keydown', handleKeyDown);

