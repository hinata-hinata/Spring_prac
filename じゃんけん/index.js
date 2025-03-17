"use strict";

const gu = document.getElementById('gu-');
const tyoki = document.getElementById('tyoki');
const pa = document.getElementById('pa-');
const enemy = document.getElementById('enemy');
const enemy_hand = ['gu-.jpg', 'pa-.jpg', 'tyoki.jpg'];
const img = document.createElement('img');
let imgIndex;

gu.addEventListener('click', function(){
  tyoki.style.display = 'none';
  pa.style.display = 'none';

  enemy_pon();
})

tyoki.addEventListener('click', function(){
  gu.style.display = 'none';
  pa.style.display = 'none';

  enemy_pon();
})

pa.addEventListener('click', function(){
  tyoki.style.display = 'none';
  gu.style.display = 'none';

  enemy_pon();
})

function enemy_pon(){
  imgIndex = Math.floor(Math.random() * 3);
  img.src = enemy_hand[imgIndex];
  enemy.appendChild(img);
}