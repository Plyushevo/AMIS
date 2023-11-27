import time
# Lesson 3 tasks
# Test all of your functions by calling them. return is not needed unless specified.
# Feel free to rename the functions
# Remove pass before writing anything in the function

# Task 1
# Create a function that asks the user for a name. Using only one f-string, display the text "Hello, {name}! How are you?" on two lines.

def hello_user():
    name = input('What is your name?: ')
    return print(f"Hello, {name}!\nHow are you?")
hello_user()
# Create a function that asks the user for a temperature. If the temperature is over 30 and under 35, print "It's a hot day, stay cool"
# If the temperatre is over 15 and under 30 print "Nice weather for a walk"
# If the temperature is between 15 and 0, print "It's quite chilly, dress warmly"
# If the temperature is under 0 and above -20, print "It's freezing, stay warm"
# If the temperature is -20 or less, or 35 or above, print "Extreme weather, stay safe"

# Task 2

def temperature_checker():
    temp = int(input('What is current temperature?: '))
    if 30 <= temp <35:
        print("It's a hot day, stay cool")
    elif 15 <= temp < 30:
        print("Nice weather for a walk")
    elif 0 <= temp < 15:
        print("It's quite chilly, dress warmly")
    elif -20 <= temp < 0:
        print("It's freezing, stay warm")
    else:
        print("Extreme weather, stay safe")
temperature_checker()

# Task 3

# Ask the user to enter a number.
# Using a for loop, print out the multiplication table for that number from 1 to 10.
# Each line should show the calculation, for example: "3 x 4 = 12".
# Example output: 
# Input a number 5
# 1 x 5 = 5 
# 2 x 5 = 10
# 3 x 5 = 15
# 4 x 5 = 20
# 5 x 5 = 25
# 6 x 5 = 30
# 7 x 5 = 35
# 8 x 5 = 40
# 9 x 5 = 45
# 10 x 5 = 50

def multiplication_table():
    userNumber = int(input('Please enter a number: '))
    print(f"Input number {userNumber}")
    for i in range(userNumber):
        i += 1
        print(f"{i} x {userNumber} = {i * userNumber}")
        
multiplication_table()
# Task 4

# Write a program that checks if a number entered by the user is even or odd.
# Output True if the number is even, and False if the number is odd.

def even_or_odd():
    print(f"Even or odd?")
    userNumber = int(input('Please enter a number: '))
    if userNumber % 2 == 0:
        print('Number is odd?', True)
    else:
        print('Number is odd?', False)
even_or_odd()
# Task 5

# Create a program that starts with an empty list named shopping_list.
# Have the user enter a series of items to add to the list, one at a time.
# If the user enters 'DONE', print out the list and end the program.
# Use loops in this exercise. A while loop is good.

def shopping_list():
    shopping_list = []
    userInput = input('Enter an item to buy: ')
    while userInput != 'DONE':
        shopping_list.append(userInput)
        print(f"You need to buy: {shopping_list}")
        userInput = input('Enter an item to buy: ')
    print(f"you're DONE, your list is: {shopping_list}")
shopping_list()
# Task 6

# Write a program that asks the user to enter a number of seconds for a countdown.
# Using a while loop, count down to zero from the given number, printing each number.
# You can use time.sleep() for this, remember to import the module time to use this method. 
# When the countdown reaches zero, print "Time's up!".

def countdown_timer():
    userThreshold = int(input('Enter a countdown time: '))
    i = 0
    while i in range(userThreshold):
        print(userThreshold - i)
        i += 1
        time.sleep(1)
    print('Time\'s up!')
countdown_timer()
# Task 7

# Create a program that validates user password input.
# Set up conditions for a valid password: must include a number, a capital letter, and be at least 8 characters long.
# Ask the user to enter a password and output True if it meets the conditions and False if it doesn’t. You can also write your own messages for True and False.
# Hint: you can use these in your if-statement: 
# is_upper = any([c.isupper() for c in password])
# is_digit = any([c.isdigit() for c in password])
# For more information on how this works, google: python list comprehension. Another thing to google: python any

def password_validator():
    reTipe = True
    while reTipe:
        is_upper = any([c.isupper() for c in password])
        is_digit = any([c.isdigit() for c in password])
        password = input('Enter a password here: ')
        if len(password) >= 8:
            if is_upper:
                if is_digit:
                    print('You have a good password!')
                    reTipe = False
                else:
                    print('You need at least 1 digit in your password!')
            else:
                print('You need at least 1 Uppercase letter')        
        else:
            print("Your password is too short")

password_validator()