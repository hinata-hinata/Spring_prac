"use strict";

const contain = document.getElementById('contain');
let miss_type = 0;
const overlay = document.getElementById('overlay');
const closeoverlay = document.getElementById('closeoverlay');
const reload = document.getElementById('reload');



const normal = document.getElementById('normal');
normal.addEventListener('click', function () {
  while (contain.firstChild) {
    contain.removeChild(contain.firstChild);
  }

  const message = document.createElement('div');
  message.textContent = 'Press Enter Key';
  message.classList.add('message_style');
  contain.appendChild(message);

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
      startCountdown();
    }
  })
});

function startCountdown() {
  const message = contain.firstChild;
  contain.removeChild(message);
  let count = 3;
  const countdown = document.createElement('div');
  countdown.classList.add('countdown_style')
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
  spell.classList.add('randomspell_style');
  contain.appendChild(spell);

  const inputarea = document.createElement('input');
  inputarea.classList.add('inputarea_style');
  contain.appendChild(inputarea);
  inputarea.focus();
  const miss_type_text = document.createElement('div');
  miss_type_text.textContent = `ミスタイプ数 : ${miss_type}`;
  miss_type_text.classList.add('misstype_style');
  contain.appendChild(miss_type_text);

  const stopButton = document.createElement('button');
  stopButton.textContent = '一時停止';
  stopButton.classList.add('stopbtn');
  contain.appendChild(stopButton);

  stopButton.addEventListener('click', function(){
    overlay.style.display = 'flex';
  })

  closeoverlay.addEventListener('click', function(){
    overlay.style.display = 'none';
  })

  reload.addEventListener('click', function(){
    location.reload();
  })

  let prevLength = 0;
  inputarea.addEventListener('input', function () {
    const s = inputarea.value;
    for (let i = prevLength; i < s.length; i++) {
      if (s[i] !== random_spell[i]) {
        miss_type += 1;
      }
    }
    prevLength = s.length;
    miss_type_text.textContent = `ミスタイプ数 : ${miss_type}`;

    if (s === random_spell){
      game_main();
    }
  })

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