# Lesson 4 tasks
# Test all of your functions by calling them. return is not needed unless specified.
# Feel free to rename the functions
# Remove pass before writing anything in the function
# After you finish a task, comment out the function call to speed up your work
# Don't overthink the assignments, just ask if there are any questions 

# Task 1
# a)
# Create a dictionary named pet_info that has keys for "name", "species", "age" and
# "favorite food"
# Fill in the values with information about a pet
# Print the dictionary

# b)
# Print only the name

# c)
# Change the age of the pet, print it to test

# d)
# d1) Add a key-value pair called "other_info" to pet_info
# d2) Delete other_info

# Task 2
# Create a function that takes input from the user
# Create a file in the same folder you have saved your exercise in
# You can create the file manually, or inside your function
# Make your function write the input from the user into the file
# Keywords: file write, with open

def note_to_self():
    pass

# Task 3
# Ask the user for input, instruct them to write about what happened today
# Create a function that writes to a file you have created 
# You should append to the file, not overwrite it
# Test with calling the function repeatedly
# The existing entries shouldn't be deleted with new entries

def add_to_daily_log():
    pass

# Task 4
# Create an empty list
# Ask the user to input names, and tell them how to stop the program
# When the user inputs "done", the program stops and prints all the names
# Hint: you can use the list methods append and join for this exercise

def party_invite_list():
    pass

# Task 5
# Create an empty dictionary called movie inside the function movie_info()
# With 3 input calls, ask the user to add values to the keys "title", "year" and "rating" to the dictionary
# After taking the input, print the info in a way, that the key names are capitalized, and the values formatted
# Hint: you can use a for in loop to loop through the info: for key, value in info.items():

def movie_info():
    pass

# Task 6
# Create a function that shows the current time
# Try to show the time in a human-readable format
# You can use the time module

def show_current_time():
    pass

# Task 7
# Create a list with bad words
# Write a function that asks the user to input a sentence that contains the bad words
# Print or return the sentence with all of the bad words replaced with stars *****
# As a bonus, try to make the number of stars the same as the amount of letters in the censored word
# One way to do this is to loop through the bad words and test if they are found in the sentence
# The string replace method can be useful here

bad_words=["fuck", "ass", "cunt"]

def censor_profanities():
    userInput = str(input("input a sentence that contains the bad words: "))
    for word in bad_words:
        if word in userInput:
            censor = len(word) * "*"
            userInput = userInput.replace(word, censor)
    print(userInput)    
    
    
#censor_profanities()



# Extra task
import time
# Write a program that uses the time module to create a workout timer
# The user can input different exercises and the duration for each
# The program will then ask the user to press enter to start an exercise
# During the exercise, time remaining will be displayed
# When the exercise ends, tell the user the exercise is finished
# Proceed to the next exercise, repeat the process until no exercises remain
# When the workout ends, notify the user that the workout is complete
# Bonus: Prepare for invalid user input. Handle errors.

def workout_timer():
    workout = {}
    userExercise = str(input("enter an exersise name, write done to end: "))
    
    while userExercise.lower() != "done":
        try:
            exerciseTime = int(input("enter an exersise time (s): "))
            workout[userExercise] = exerciseTime
        except ValueError:
            print("Pleaase enter a valid integer for exercise time")
        userExercise = str(input("enter an exersise name, write done to end: "))
    
    if not workout:
        print("No exercise entered. Exiting")
        return
        
    input("press 'Enter' to start workout")
    for exercise, duration in workout.items():
        print(f"starting {exercise} for {duration} seconds...")
        time.sleep(1)
        for i in range(duration, 0, -1):
            print("time left:", i)
            time.sleep(1)
        input("press 'Enter' to start next exercise")
    
    print("Workout complete!")
            
workout_timer()