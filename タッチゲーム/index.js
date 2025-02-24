"use strict";

const normalBtn = document.getElementById('button_normal');
const gameMain = document.getElementById('game_main');
let now = 1;
let items = [];

normalBtn.addEventListener('click', function () {
  game_start();
  game_main();
})


function game_start() {
  while (gameMain.firstChild) {
    gameMain.removeChild(gameMain.firstChild);
  }

  items = [];
  // ランダムに並び替える
  let num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
  num_list.sort(function () {
    return Math.random() - 0.5;
  });

  num_list.forEach(function (number) {
    const item = document.createElement('button');
    item.textContent = number;
    item.classList.add('item_style');
    gameMain.appendChild(item);
    items.push(item);
  })
  gameMain.classList.add('grid');
}

function game_main() {
  items.forEach(function (item) {
    item.addEventListener('click', function () {

      if (now === parseInt(item.textContent)) {
        now += 1;
        item.classList.add('clicked_btn');
      }
      if(now>9){
        window.alert('すばらしい!!');
        setTimeout(reload, 600);
      }
    });
  });
}

function reload(){
  location.reload();
}


