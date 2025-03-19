"use strict";

const gu = document.getElementById('gu-');
const tyoki = document.getElementById('tyoki');
const pa = document.getElementById('pa-');
const enemy = document.getElementById('enemy');
const enemy_hand = ['gu-.jpg', 'pa-.jpg', 'tyoki.jpg'];
const img = document.createElement('img');
const judgeText = document.getElementById('judge');
let imgIndex;
let my_pon;
let enemy_pon;


gu.addEventListener('click', function () {
  tyoki.style.display = 'none';
  pa.style.display = 'none';
  my_pon = 'gu-';

  enemy_action();
  judge();

})

tyoki.addEventListener('click', function () {
  gu.style.display = 'none';
  pa.style.display = 'none';
  my_pon = 'tyoki';

  enemy_action();
  judge();
})

pa.addEventListener('click', function () {
  tyoki.style.display = 'none';
  gu.style.display = 'none';
  my_pon = 'pa-';

  enemy_action();
  judge();
})

function enemy_action() {
  imgIndex = Math.floor(Math.random() * 3);
  if (imgIndex === 0) {
    enemy_pon = 'gu-';
  } else if (imgIndex === 1) {
    enemy_pon = 'pa-';
  } else {
    enemy_pon = 'tyoki';
  }
  img.src = enemy_hand[imgIndex];
  enemy.appendChild(img);
}

function judge() {
  if (my_pon === 'gu-') {
    if (enemy_pon==='tyoki'){
      judgeText.textContent = 'あなたの勝利です';
    }else if(enemy_pon==='pa-'){
      judgeText.textContent = 'あなたの負けです';
    }else{
      judgeText.textContent = 'あいこです';
    }
  }else if(my_pon==='tyoki'){
    if(enemy_pon==='pa-'){
      judgeText.textContent = 'あなたの勝利です';
    }else if(enemy_pon==='gu-'){
      judgeText.textContent = 'あなたの負けです';
    }else{
      judgeText.textContent = 'あいこです';
    }
  }else{
    if(enemy_pon==='gu-'){
      judgeText.textContent = 'あなたの勝利です';
    }else if(enemy_pon==='tyoki'){
      judgeText.textContent = 'あなたの負けです';
    }else{
      judgeText.textContent = 'あいこです';
    }
  }
  setTimeout(reload, 1000);
}

function reload(){
  location.reload();
