"use strict";

const easy = document.getElementById('easy');
const normal = document.getElementById('normal');
const hard = document.getElementById('hard');
const container = document.getElementById('container');
const source = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
let q = '';  //問題
const q_disp = document.createElement('div');
const input = document.createElement('input');  //回答欄
const okno = document.createElement('div');
let level;
const overlay = document.getElementById('overlay');
const closeBtn = document.getElementById('close');
const reloadBtn = document.getElementById('reload');
const stopBtn = document.createElement('button');


easy.addEventListener('click', function () {
  level = 0;
  all_delete();
  easy_question();
})

normal.addEventListener('click', function () {
  level = 1;
  all_delete();
  normal_question();
})

hard.addEventListener('click', function () {
  level = 2;
  all_delete();
  hard_question();
})

//入力があったときに判定
input.addEventListener('input', function () {
  if (q === input.value) {
    okno.textContent = 'ok';
    okno.classList.add('okno_style');
    container.appendChild(okno);

    if (level === 0) {
      setTimeout(easy_question, 1000);
    } else if (level === 1) {
      setTimeout(normal_question, 1000);
    }else{
      setTimeout(hard_question, 1000);
    }
  }
})

function all_delete() {
  while (container.firstChild) {
    container.removeChild(container.firstChild);
  }
  container.classList.add('container_back');
}

//問題の作成
function easy_question() {
  q = '';
  input.value = '';
  okno.textContent = '';
  for (let i = 0; i < 3; i++) {
    const a = Math.floor(Math.random() * 9);
    q += source[a];
  }
  q_disp.textContent = q;
  q_disp.classList.add('q_style');
  container.appendChild(q_disp);
  //1秒後に問題を消す
  setTimeout(() => {
    q_disp.textContent = '';
  }, 1000);

  judge();
  over();
}

function normal_question() {
  q = '';
  input.value = '';
  okno.textContent = '';
  for (let i = 0; i < 5; i++) {
    const a = Math.floor(Math.random() * 9);
    q += source[a];
  }
  q_disp.textContent = q;
  q_disp.classList.add('q_style');
  container.appendChild(q_disp);
  //1秒後に問題を消す
  setTimeout(() => {
    q_disp.textContent = '';
  }, 900);

  judge();
  over();
}

function hard_question() {
  q = '';
  input.value = '';
  okno.textContent = '';
  for (let i = 0; i < 6; i++) {
    const a = Math.floor(Math.random() * 9);
    q += source[a];
  }
  q_disp.textContent = q;
  q_disp.classList.add('q_style');
  container.appendChild(q_disp);
  //1秒後に問題を消す
  setTimeout(() => {
    q_disp.textContent = '';
  }, 900);

  judge();
  over();
}

function judge() {
  input.classList.add('input_style');
  container.appendChild(input);
  input.focus();
}

//オーバーレイ実装
function over() {
  stopBtn.textContent = 'STOP';
  stopBtn.classList.add('stop_style');
  container.appendChild(stopBtn);

  stopBtn.addEventListener('click', function () {
    overlay.style.display = 'flex';
  })

  closeBtn.addEventListener('click', function () {
    overlay.style.display = 'none';
  })

  reloadBtn.addEventListener('click', function(){
    location.reload();
  })
}
