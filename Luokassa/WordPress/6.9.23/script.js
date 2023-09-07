// const radioChose = document.getElementsByName('answer[8]')

// const finalButton = document.querySelector('.button.basic-vote-button')


// const voteButtons = document.querySelectorAll('#john, #will, #andrew, #kirill, #grigori, #daniil')

// let voteForMe = () => {
//   finalButton.click
// }

// function returnVoteValue () {
//   let 
// }

// let choseYourCandidate = () => {
//   const selectedCandidate = this.id
//   voteButtons.addEventListener('click', {

//   })
// }


const radioChose = document.getElementsByName('answer[8]');
const finalButton = document.querySelector('.button.basic-vote-button');
const voteButtons = document.querySelectorAll('#john, #will, #andrew, #kirill, #grigori, #daniil');

console.log(radioChose, finalButton, voteButtons)

// Функция для обработки нажатия кнопок кандидатов
function handleCandidateButtonClick(candidateId) {
  // Находим соответствующую радио кнопку в списке radioChose
  const radioInput = radioChose.find((radio) => radio.value === candidateId);
  
  if (radioInput) {
    // Устанавливаем радио кнопку в состояние выбранной
    radioInput.checked = true;
  }
}

// Добавляем обработчик события для каждой кнопки кандидата
voteButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const candidateId = button.id;
    handleCandidateButtonClick(candidateId);
  });
});

// Добавляем обработчик события для главной кнопки голосования (если это необходимо)
finalButton.addEventListener('click', () => {
  // Ваш код для обработки голосования
});

// Добавляем обработчик события для каждой кнопки кандидата
voteButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const candidateId = button.id;
    handleCandidateButtonClick(candidateId);
  });
});

// Добавляем обработчик события для главной кнопки голосования (если это необходимо)
finalButton.addEventListener('click', () => {
  // Ваш код для обработки голосования
});
