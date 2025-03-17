"use strict";;

const contain = document.getElementById('contain');
const easy = document.getElementById('easy');
const normal = document.getElementById('normal');
const count_num = document.createElement('div'); //カウントの数字を入れるdiv
let count = 3;
let level;
// let num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
let enemy_num;
const enemy_num_div = document.createElement('div');
let my_num;
const my_num_div = document.createElement('div');
const card_div = document.createElement('div');
let score = 0;


easy.addEventListener('click', function () {
  //難易度を分けるためにフラグを立てておく
  level = 0;

  all_delete();
  count_down();

})

normal.addEventListener('click', function () {
  level = 1;

  all_delete();
  count_down();
})

//containのすべての要素の削除
function all_delete() {
  while (contain.firstChild) {
    contain.removeChild(contain.firstChild);
  }
}

//カウントダウン321
function count_down() {
  if (count > 0) {
    count_num.textContent = count;
    contain.appendChild(count_num);
    count -= 1;
    setTimeout(count_down, 1000);
  } else {
    count_num.textContent = 'Start!';

    //ゲーム開始
    setTimeout(level_call, 1000);
  }
}

//levelの数字で呼び出し先を変える
function level_call() {
  all_delete();

  if (level === 0) {
    easy_game();
  } else if (level === 1) {

  }
}

function easy_game() {
  if (score < 11) {
    all_delete();
    //敵のカード
    enemy_num = Math.floor(Math.random() * 13) + 1;
    enemy_num_div.textContent = enemy_num;
    enemy_num_div.classList.add('enemy_num_style');
    contain.appendChild(enemy_num_div);

    //味方のカード
    my_num = Math.floor(Math.random() * 13) + 1;
    my_num_div.textContent = my_num;
    my_num_div.classList.add('my_num_style');
    my_num_div.classList.add('black_style');
    contain.appendChild(my_num_div);

    //選択ボタン
    const highBtn = document.createElement('button');
    const lowBtn = document.createElement('button');
    highBtn.textContent = 'High';
    lowBtn.textContent = 'Low';

    highBtn.addEventListener('click', function () {
      judge_high();
      highBtn.disabled = true;
      lowBtn.disabled = true;
    })
    lowBtn.addEventListener('click', function () {
      judge_low();
      highBtn.disabled = true;
      lowBtn.disabled = true;
    })

    contain.appendChild(highBtn);
    contain.appendChild(lowBtn);

    const next = document.createElement('button');
    next.textContent = '次へ';
    next.classList.add('next_style');
    next.addEventListener('click', function () {
        easy_game();
    })
    contain.appendChild(next);

    const score_div = document.createElement('div');
    score_div.textContent = score;
    score_div.classList.add('score_style');
    contain.appendChild(score_div);
  } else {
    alert('終了です！');
    location.reload();
  }
}

function judge_high() {
  if (my_num >= enemy_num) {
    alert('あなたの勝ちです!');
    score += 1;
  } else {
    alert('あなたの負けです');
    setTimeout(function () {
      location.reload();
    }, 500);
  }
  // score_div.textContent = score;
  my_num_div.classList.remove('black_style')
}

function judge_low() {
  if (my_num >= enemy_num) {
    alert('あなたの負けです');
    setTimeout(function () {
      location.reload();
    }, 500);

  } else {
    alert('あなたの勝ちです!');
    score += 1;
  }
  // score_div.textContent = score;
  my_num_div.classList.remove('black_style')
}