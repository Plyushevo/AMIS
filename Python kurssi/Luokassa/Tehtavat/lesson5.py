# Lesson 5 tasks
# Test all of your functions by calling them. return is not needed unless specified.
# Feel free to rename the functions
# Remove pass before writing anything in the function
# After you finish a task, you can comment out the function call to speed up your work

# 1
# Write a program that helps to plan weekend activities based on weather
# True represents a sunny day. False represents a rainy day.
# Display a message for each of these conditions:
# All days are sunny, all days are rainy, some days are sunny
# Test your function with these 3 predefined lists
# One way to solve this is to do an if-elif statement for different any and all results

weekend1_weather=[True, False, True]
weekend2_weather=[False, False, False]
weekend3_weather=[True, True, True]

def activity_planner(weather):
    if True not in weather:
        print("rainee day")
    elif False not in weather:
        print("Sunie day")
    else:
        print("Sometimes it is rainee")

#activity_planner(weekend3_weather)
# 2
# a)
# You are planning a trip with your friend
# You have 2 lists: a destination list from you, and another from your friend
# Combine the 2 lists and sort them alphabetically
# One way to do this is by using the list extend method
# You can use these 2 lists or make your own

destinations1=["Madrid", "Valencia", "Andorra", "Malaga", "Murcia"]
destinations2=["Paris", "Lyon", "Monaco", "Toulouse", "Caen"]

def destination_list(list1, list2):
    list3 = list1 + list2
    list3.sort()
    print(list3)
    list3.pop(-1)
    print(list3)
#destination_list(destinations1, destinations2)
# b)
# Using the pop method, remove and print the last city on the combined list
# You can do this inside the function you created or outside of it, the main thing here is to use the List pop method

# print(destination_list(destinations1, destinations2))

# 3
# Create a coin toss simulation with a 50/50 chance of success
# Import the random module to be able to generate random numbers
# Based on chance, print out a sentence/word describing heads or a sentence/word describing tails
# You can use random.choice() here
import random
def coin_toss():
    user_input = input('Нажми на Enter чтобы бросить монету, нажми q чтобы выйти ')
    heads = 0
    tails = 0
    total = 0
    while user_input != 'q':
        coins = ['Орёл', 'Решка']
        coin = random.choice(coins)

        print(coin)
        if coin == 'Орёл':
            heads += 1
        elif coin == 'Решка':
            tails += 1
        
        user_input = input('Нажми на Enter чтобы бросить монету, нажми q чтобы выйти ')
        total += 1
    print(f"Всего подбросов: {total} Орёл: {heads} Решка {tails}")
#coin_toss()
# 4
# a)
# Create a looping program where the user enters a string, the program reverses the string and prints it
# The loop continues until the user types "q" or "quit" for example
def loop_string():
    user_input = input('pls enter a string or ty q to exit: ')
    user_strings_reversed = []
    while user_input != 'q':
        string1 = user_input[::-1]
        user_strings_reversed.append(string1)
        print(string1)
        user_input = input('pls enter a string or ty q to exit: ')
    print_all_strings = input('Do you want to print all reversed strings(y/n)? ')
    if print_all_strings.lower() == 'y':
        print(user_strings_reversed)
    else:
        print('Exiting...')
    for string in user_strings_reversed:
        capital = string.capitalize()
        print(capital)
#loop_string()
# b)
# Give the user the option to print all reversed strings
# You can additionally print all original strings 

# c)
# Capitalize all reversed strings

# 4
# Given a list of numbers with lots of decimals, create a program that prints all the numbers with the accuracy of 2 decimals
# The exact formatting of the output is up to you, as long as all of them are printed
# You can use f-strings and the syntax {number:.2f} to format the numbers to 2 decimals

decimal_list = [2.500000000, 2.511, 2.51, 5.12456526246, 2.24222222222, 1.1999999999999999999999999999999999999999999999999]

def two_decimals(list):
    for elem in list:
        print("%.2f" % elem)
#two_decimals(decimal_list)
# 5
# Create a program that turns sentences into hashtags
# Give a string as an argument, for example "The Weeknd is on tour"
# Return a modified string that has the following:
# Each word is capitalized
# Spaces are removed
# A hashtag is added to the beginning of the sentence
# Example: #TheWeekndIsOnTour

# Hints: You can use a for in loop to loop through the words or import string and use string.capwords to capitalize the letters
# The string replace method can be useful in this task

import string

def create_hashtag():
    user_input = input("Enter a phrase to make a hashtag: ").strip()
    if not user_input:
        print('pls enter a valid phrase.')
        return
    user_words = user_input.split()
    hashed = '#' + ''.join(elem.capitalize() for elem in user_words)
    print(f"Your hash tag is ready: {hashed}")    
    
    

#create_hashtag()
# 6 Bonus task
# Given a dictionary of student names and their scores, write a program to update the score of a specific student.
# To do this, ask the user to input the student's name and then ask for the number to change it to.
# Tell the user what they have to do and what is happening where necessary. For example you could tell that 
# a student was successfully selected and then print their name and grade
# Alternatively, you can implement your own system of accessing a specific student. If you want to, you can change the dictionary.
# Display the updated dictionary and test that your program works
# Try to handle incorrect input and test if you were successful by trying to input wrong values

names_and_scores = {
    "Madeleine": 5,
    "Juan": 2,
    "Mikel": 4,
    "Lanny": 1,
    "Emanuel": 3
}

def score_update(dictionary):
    while True:
        user_input = input('Pls enter student name: ').strip().capitalize()
        if user_input in dictionary:
            student_score = dictionary[user_input]
            print(f"{user_input} is found in database with score of {student_score}")
            while True:
                is_change = input(f"would you like to change {user_input}'s score? (Y/N): ").lower().strip()
                if is_change == 'y':
                    new_score = input(f"pls enter {user_input}'s new score here: ")
                    try:
                        new_score = int(new_score)
                        if 0 <= new_score <= 10 :
                            dictionary.update({user_input:new_score})
                            print(f"{user_input}'s new score is {new_score}")
                            break
                        else:
                            print(f"pls enter correct [0, 10] {user_input}'s new score here: ")
                    except ValueError:
                        print("enter a valid integer score")
                elif is_change == 'n':
                    print("No changes made")
                    break
                else:
                    print("Invalid input. pls enter 'Y or 'N")
        else:
            print(f"{user_input} hasn't found in database")
        continue_input = input("Do you want to enter another student's name (Y/N)").lower()
        if continue_input != 'y':
            break

score_update(names_and_scores)