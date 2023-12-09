// Задача о задержке:
// Создайте промис, который выполняется через 3 секунды и возвращает сообщение "Прошло 3 секунды".

// const promise1 = new Promise((resolve, reject) =>{
//   setTimeout(() => {
//     resolve("Прошло 3 секунды")
//   }, 3000)
// })

// promise1.then((value) => {
//   console.log(value)
// })

// Задача о случайном успехе:
// Создайте промис, который выполняется успешно (fulfilled) с вероятностью 50% и возвращает "Успех!" или отклоняется (rejected) с вероятностью 50% и возвращает "Неудача!".

const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    const isSuccess = Math.random() * 100 <= 50 ? resolve("Успех!") : reject("Неудача!")
  }, 1)
})
promise2
  .then((value) =>{
    console.log(value)
})
  .catch((value) =>{
    console.log(value)
})

// Задача о генерации случайного числа:
// Создайте промис, который генерирует случайное число от 1 до 10 и выполняется с этим числом.

const promise3 = new Promise((resolve, reject) => {
    const randomNum = Math.floor(Math.random() * (11 - 1) + 1 )
    resolve(randomNum)
})

promise3
  .then((value) => {
    console.log(value)
  })
// Задача о проверке числа на четность:
// Создайте функцию, которая принимает число. Если число четное, промис выполняется с сообщением "Четное число", в противном случае промис отклоняется с сообщением "Нечетное число".

const toEven = (num) => {
  return new Promise((resolve, reject) => {
    num % 2 === 0 ? resolve("Четное число") : reject("Нечетное число")
  }) 
}

toEven(10)
  .then((value) => {
    console.log(value)
  })
  .catch((value) => {
  console.log(value)
  })


// Задача о подключении к внешнему API:
// Создайте промис, который делает запрос к внешнему API (например, JSONPlaceholder) и возвращает первого пользователя в формате JSON. Обработайте случаи успешного выполнения и ошибок при запросе.

const fetchFirstUser = () => {
  return new Promise((resolve, reject) => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => {
        if (!response.ok) {
          reject(`Errorr: ${response.status}`)
          return
        }
        return response.json()
      })
      .then(users => {
        const firstUser = users[0]
        resolve(firstUser)
      })
      .catch(error => {
        reject(`error ${error}`)
      })
  })
}

fetchFirstUser()
.then(firstUser => {
  console.log('First user', firstUser)
})
.catch(error => {
  console.error('error', error)
})