"use strict";

const contain = document.getElementById('contain');
const normal = document.getElementById('normal');
normal.addEventListener('click', function () {
  while (contain.firstChild) {
    contain.removeChild(contain.firstChild);
  }

  const message = document.createElement('div');
  message.textContent = 'Press Enter Key';
  contain.appendChild(message);

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
      startCountdown();
    }
  })
});

function startCountdown() {
  let count = 3;
  const countdown = document.createElement('div');
  contain.appendChild(countdown);

  function countdownStep() {
    countdown.textContent = count;
    count -= 1;

    if (count >= 0) {
      setTimeout(countdownStep, 1000); // 1秒後にもう一度実行
    } else {
      countdown.textContent = 'Start!';
      setTimeout(game_main, 1000);
    }
  }

  countdownStep();
}

function game_main() {
  while (contain.firstChild) {
    contain.removeChild(contain.firstChild);
  }
  const random_spell = randomspell();
  const spell = document.createElement('div');
  spell.textContent = random_spell;
  contain.appendChild(spell);
}

function randomspell() {
  const spell_list = [
    'apple',
    'orange',
    'banana',
    'grape',
    'peach',
    'cherry',
    'mango',
    'pineapple',
    'strawberry',
    'blueberry',
    'kiwi',
    'watermelon'
  ];
  const randomindex = Math.floor(Math.random() * 12);
  const random_spell = spell_list[randomindex];
  return random_spell;
}