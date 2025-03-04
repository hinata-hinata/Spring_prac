"use strict";

const easyButton = document.getElementById('easy');
const contain = document.getElementById('contain');
let numlist;
let count = 0
let checkList = [];


easyButton.addEventListener('click', function () {
  nextPage();
  choseeasy();


})

function nextPage() {
  while (contain.firstChild) {
    contain.removeChild(contain.firstChild);
  }
}

function choseeasy() {
  numlist = ['1', '1', '2', '2', '3', '3', '4', '4', '5', '5'];
  numlist.sort(function () {
    return Math.random() - 0.5;
  })
  numlist.forEach(function (number) {
    const item = document.createElement('button');
    item.textContent = number;
    item.classList.add('item_style');
    item.classList.add('item_style_color');

    item.addEventListener('click', function () {
      click_button(item);
    })

    contain.appendChild(item);
  })
  contain.classList.add('grid');
}

function click_button(item) {
  count += 1
  checkList.push(item.textContent);
  item.classList.remove('item_style_color');

  if (count === 2) {
    if(checkList[0] === checkList[1]){
      alert('正解！');
    }

    alert('不正解');
    }
    

  }



