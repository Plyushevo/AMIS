// Write a function that displays the text "Moi maailma!"

const displayText = () => console.log("Moi maailma!")

// Write a function that takes an age as a parameter and logs "Access granted" 
// if the age is 18 or over, and "Access denied" if under 18.

const ageCheck = (age) => {
  age < 18 ? console.log("Access denied") : console.log("Access granted")
}

ageCheck(18)
// Write a function countToN that takes a number 
// called n as a parameter and logs numbers from 1 to n.


const countToN = (n) => {
  for (let i = 1; i <= n; i++) console.log(i)
}
countToN(10)
// Create a function subtractNumbers that takes two parameters and returns their remainder.

const subtractNumbers = (a, b) => a - b

console.log(subtractNumbers(4, 2))
// Write a function isEven that takes a number and returns true if the number is even, 
// and false if it's odd.


const isEven = (num) => {
  num % 2 === 0 ? true : false
} 
// Write a function outerFunction that defines a number variable and a nested function innerFunction. The inner function should increment the value of the variable by one 

const outerFunction = () => {
  let number = 4
  const innerFunction = () => {
    number += 1
    console.log(number)
  }
  innerFunction()
}

outerFunction()

// and then log it to the console. 
// Call innerFunction from within outerFunction, then call outerFunction.