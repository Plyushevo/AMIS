// Welcome to arrays and loops!
// Please do these exercises by creating an HTML file and connecting this file to it using <script src="arrays_and_loops"></script>
// Place the tag after </body>
// You can display the results in the browser console (dev tools), or in your HTML file.
// console.log("If you see this in your browser's console, you can remove this message from the JS file and start doing the exercises")

// 1
// Create an Array: Define an array named colors containing three strings, 
// each representing a color (e.g., "red", "green", "blue").
// Display the array you created
const colors = ["red", "green", "blue"]
console.log(colors)
// 2
// Access Array Elements: Given an array of numbers, 
// a) Write code to print the third element of the array.
// b) Display the last element in the array
numArr = [1, 2, 3, 4, 5];
console.log(numArr[2])
console.log(numArr.pop())
console.log(numArr)
// 3
// Basic While Loop: Write a while loop that prints numbers from 1 to 5.
console.log("Basic While Loop")
i = 0
while (i < 5) {
  i++
  console.log(i)
  
}

// 4
// Basic For Loop: Write a for loop that prints numbers from 1 to 5.
console.log("Basic For Loop")
for (let i = 1; i <= 5; i++) console.log(i)

// 5
// Using .length, get the length of the given string and display it.
let str1 = "Kenkäkauppa"
console.log(`${str1} length is ${str1.length}`)
// 6
// Iterate Over an Array: Using a for loop, iterate through an array of strings 
// and print each string.
let array1 = ["apple", "cherry", "banana"]
for (fruit of array1) console.log(fruit)
// 7
// Type Conversion:
// Convert the string "1234" into an integer and the number 5678 into a string. Assign these to variables.
// Note: you can use the methods Number() and String() 
// Test that you got it right by using the typeof operator on the variables (you can display the result in the console).
let stringNumber = "1234"
let numberNumber = 5678

stringNumber = Number(stringNumber)
numberNumber = numberNumber.toString()

console.log(typeof(stringNumber), typeof(numberNumber))
// 8
// Use push() to add an extra element to weatherArray.
// Display the array and test that the element was successfully added 
let weatherArray = ["Sunny", "Cloudy", "Stormy", "Foggy"]
weatherArray.push('Stormy')
console.log(weatherArray)
// 9
// Sum of Array Elements: 
// Create an array that contains numbers. 
// Write a function that takes an array of numbers as an argument and returns the sum of all elements.

function sumElements(array){
  let sum = 0
  for (elem of array) {
    sum += elem
  }
  console.log(sum)
}
sumElements(numArr)
// 10
// Basic Login System:
// Create a simple login system where the user inputs a username and password. 
// You can use prompt() to get input from the user, or you can implement actual login input fields.
// If the username is "admin" and the password is "12345", print "Login successful". Otherwise, print "Login failed".
// Tips: You can use a function and call it. One way to succeed is to set up variables that contain the correct name and password 
// and test user input against these values. Console.log or otherwise return/display the results.
const usersArray = {
  'admin': '12345',
  'kirill': '12345'
}

// const loginForm = document.getElementById("loginForm")
// loginForm.addEventListener("submit", (event) => {
//   event.preventDefault()

//   let username = document.getElementById("username")
//   let password = document.getElementById("password")

//   if (username.value in usersArray && usersArray[username.value] === password.value) alert("You're logged in")
//   else alert("Login failed")
// })
  
// 11
// Filter Even Numbers: 
// Write a function that takes an array of numbers as an argument and returns an array containing only the even numbers.
// To test for if a number is odd, you can the modulus % operator like this: if (number % 2 === 0).
// To achieve this, you may create an empty array and use push() inside a loop to add even numbers to the new array.
// You can then return or console.log the new array
const numberArr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
const filterEven = (array) => {
  let filtered = []
  for (num of array) {
    if (num % 2 === 0) {
      filtered.push(num)
    }

  }
  console.log(filtered)
}

filterEven(numberArr5)
// 12
// Write a function arrayLength that returns the length of an array passed to it as an argument.
let clothesArray = ["hat", "trousers", "shirt", "gloves", "socks"]
const arrayLength = () => {
  
}