// Write a function reverseArray that takes an array and 
// returns a new array with the elements in reverse order.
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const reverseArray = (array) => {
  let reversedArray =[]
  for (let i = array.length - 1; i >= 0; i--) {
    reversedArray.push(array[i])
  }
  console.log(reversedArray)
}
reverseArray(arr)
// Check for Duplicates: Write a function that checks if an array 
// contains any duplicates and returns true or false.
// Using a combination of filter and indexOf can work here
let carArray = ["Mercedes-Benz", "Audi", "Toyota", "Toyota", "Lamborghini"];

const ifDuplicates = (array) => {
  const duplicates = array.filter((item, index) => {
    const isFirstTime = array.indexOf(item) === index
    return !isFirstTime
  })
  console.log(duplicates)
}

ifDuplicates(carArray)
// Array Intersection: Given two arrays, write a function that returns a new array 
// containing elements common to both arrays.
// Using a combination of filter and indexOf can also work here
let numArr1 = [22, 44, 66, 77, 45];
let numArr2 = [33, 41, 61, 77, 45];

const returnCommon = (array1, array2) => {
  const duplicates = []
    array1.forEach((elem) => {
      if (array2.includes(elem)) {
        duplicates.push(elem)
      }
    })
  console.log(duplicates)
}

returnCommon(numArr1, numArr2)

const returnCommonIndexOf = (array1, array2) => {
  const duplicates = array1.filter((item) =>{
    const duplicate = array2.indexOf(item) !== -1 
    return duplicate
  })
  console.log(duplicates)
}

returnCommonIndexOf(numArr1, numArr2)
// Create a function that assigns a number grade (1, 2, 3, 4, 5) 
// based on a student's score. Assume the score is an integer between 0 and 100.
// Example grading: 1-19: 1, 20-39: 2, 40-59: 3, 60-79: 4, 80-100: 5
let students = [
{"Mia": 77},
{"Joey": 45},
{"Aziz": 95},
{"Jonne": 12}
]

const assignGrade = (obj) => {
  for (const [key, value] of Object.entries(obj)){
    if (value <= 19) obj[key] = 1
    else if (value > 20 && value <39) obj[key] = 2
    else if (value > 39 && value <59) obj[key] = 3
    else if (value > 59 && value <79) obj[key] = 4
    else if (value > 79) obj[key] = 5
    else console.log("wrong value")
  }
  return obj
}

const assignStudents = (students) => {
  const scores =students.map((student) => assignGrade(student))
  console.log(scores)
}
console.log(students)
assignStudents(students)
// Average value
// Create an array of numbers
// Implement a function calculateAverage that takes the array of numbers
// and returns the average of the elements.
const numArr3 = [22, 44, 66, 77, 45]

const calculateAverage = (array) => {
  let sum = 0
  
  for (elem of array) sum += elem
  const average = sum / array.length
  console.log(average)
}
calculateAverage(numArr3)

const calculateAverageForEach = (array) => {
  let sum = 0
  
 array.forEach((elem) => sum += elem) 
  const average = sum / array.length
  console.log(average)
}
calculateAverageForEach(numArr3)