// 1
// Create variables of the types String, Number, Boolean.
// Console.log the types of these variables using typeof.
const str = 'string' 
const num = 3 
const bool = true

console.log('1. ' + typeof(str),typeof(num),typeof(bool))

// 2
// Create a variable that contains the number 5.
// Using the ++ operator, increase the value until it's 10, then print (console.log) the variable.
// Note that you will need many rows for this.
let i = 5
for (i; i < 10; i++){
}
console.log('2. '+ i)

// 3
// Create two string variables, firstName and lastName. 
// Concatenate them using the + operator to form and display a full name.
const firstName = 'Kirill'
const lastName = 'Belkov'
const fullName = '3. ' + firstName + ' ' + lastName
console.log(fullName)


// 4
// Create a script with an if-else statement that evaluates 
// a variable containing a temperature (e.g., 22). If the temperature is above 30, print "It's very hot",
// if it's below 10, print "It's very cold". Otherwise, print "The weather is pleasant".

const whatTemprature = (temp) => {
  if(temp > 30) console.log("4. It's very hot")
  else if(temp < 10) console.log("4. It's very cold")
  else if(temp >= 10 && temp <= 30) console.log("It's very cold")
  else console.log("4. wrong temperature type")
}

whatTemprature("fafa")
// 5
// Create a variable that contains the number 10
// Write an expression using the += compound addition operator that changes the value of the variable you created to 20. 

let num1 = 10
num1 += 10
console.log(`5. Changed the value of the num1 to ${num1}`)

// 6
// Write a script that converts the string 'false' to a boolean value (true or false).
// Verify the conversion by checking the type of the result. You can use typeof for this.
let falseString = "FalSe";

const toBoolean = (a) => {
  if (a.toLowerCase().trim() === 'false'){
    a = false
  }
  else {
    a = Boolean(a)
  }
  console.log(`6. your variable is ${a} and its type is ${typeof(a)} `)
}
toBoolean(falseString)

// 7
// Create a for loop that prints the sentence "Still looping" 5 times.
//console.log('7. ')
for(let i = 0; i < 5; i++) {
  if (i === 0) console.log('7. Still looping')
  console.log('Still looping')
}



// 8
// Use a while loop to print the numbers from 10 down to 1 in reverse order.
// After the loop finishes, print a message that says Zero.
console.log('8. 10-1')
i = 10
while (i > 0) {
  console.log(i)
  i--
}
console.log('Zero')
// 9
// a) Create an array that contains 5 colors you like.
console.log('9.')
const colors = ['white', 'blue', 'yellow', 'grey', 'green']

// b) Create a for loop that iterates over the array.
// and prints each color's name along with its position in the array (e.g., "1. Blue").

colors.forEach(function(color, index)  {
  console.log(`${index}. ${color}`)
})

// 10
// Compare null and undefined using == and ===.
// Print the results to understand how these values are compared in JavaScript.
console.log('10.')
console.log(null == undefined)
console.log(null === undefined)

// 11
// a) Write an expression that calculates the average of three numbers and prints the result.
// For example: (4 + 9 + 15) / 3;
// JavaScript has operator precedence for * and / compared to + and -. 
// This is why () should be added around the operations if you want to do them first. 

// b) Place the expression inside a function, and replace the number values with variables that are passed in as arguments.
// You can use this function skeleton:
function averageOfThree(num1, num2, num3) { // num1, num2 and num3 are the parameters for this function 
  const average = (num1 + num2 + num3) / 3
  return average
}

console.log('11. average of given 3 numbers is ' + averageOfThree(1,2,3))

// 12
// Write a function that declares a local variable named color and sets its value to 'blue'. 
// Outside this function, declare a global variable also named color but with the value 'red'. 
// Call the function and then print the value of the color variable to see how scope affects it.

const declareColor = () => {
  const color = 'blue'
  return color
}
const color = 'red'

console.log(`12. function variable value is ` + declareColor() + ' global variable value is ' + color)

// 13
// Write a function stringToNumber that takes a string as an argument. 
// If the string can be converted to a number, return the number; otherwise, return the message "Invalid number".

const stringToNumber = (str) => {
  
  str = str.replace(/\s/g, '') * 1
  console.log(str)
  if (str === NaN)
    console.log("13. Invalid number")
  console.log('13. ' + str)
}
stringToNumber('12.3                     79141241=1247=124157-1')
// 14
// Create a script that iterates over an array of numbers. 
// If a number is odd, print "Odd number: [number]"; if it's even, print "Even number: [number]".
for (let i = 0; i < 25; i++) {
  const message = i % 2 === 0 ? `Even number: [${i}]` : `Odd number: [${i}]`
  console.log(message)
}


