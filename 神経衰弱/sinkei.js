"use strict";

const contain = document.getElementById('contain');
const easyBtn = document.getElementById('easy');
const normalBtn = document.getElementById('normal');
let num_list_easy = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6];
let num_list_normal = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12];
let count_num = [];


easyBtn.addEventListener('click', function () {
  all_delete();
  set_card_easy();
})

normalBtn.addEventListener('click', function(){
  all_delete();
  set_card_normal();
})


function all_delete() {
  while (contain.firstChild) {
    contain.removeChild(contain.firstChild);
  }
}


function set_card_easy() {
  num_list_easy.sort(function () {
    return Math.random() - 0.5;
  })
  num_list_easy.forEach(function (item) {
    const button = document.createElement('button');
    button.textContent = item;
    button.classList.add('item_style');
    button.classList.add('item_style_color');
    button.addEventListener('click', function () {  //押されたとき数字を表示
      button.classList.remove('item_style_color');
      button.disabled = true;
      count_num.push(button);          //ボタンそのものを追加
      if (count_num.length === 2) {
        if (count_num[0].textContent === count_num[1].textContent) {
          count_num = [];
        } else {
          setTimeout(not_match_num, 1000);
        }

      }
    })
    contain.appendChild(button);
  })
  contain.classList.add('grid_easy');
}

function set_card_normal() {
  num_list_normal.sort(function () {
    return Math.random() - 0.5;
  })
  num_list_normal.forEach(function (item) {
    const button = document.createElement('button');
    button.textContent = item;
    button.classList.add('item_style');
    button.classList.add('item_style_color');
    button.addEventListener('click', function () {  //押されたとき数字を表示
      button.classList.remove('item_style_color');
      button.disabled = true;
      count_num.push(button);          //ボタンそのものを追加
      if (count_num.length === 2) {
        if (count_num[0].textContent === count_num[1].textContent) {
          count_num = [];
        } else {
          setTimeout(not_match_num, 1000);
        }

      }
    })
    contain.appendChild(button);
  })
  contain.classList.add('grid_normal');
}


function not_match_num() {
  count_num[0].classList.add('item_style_color');
  count_num[1].classList.add('item_style_color');
  count_num[0].disabled = false;
  count_num[1].disabled = false;
  count_num = [];
}