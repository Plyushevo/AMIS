# Import required modules from pynput.keyboard and time
import time
from pynput.keyboard import Key, Listener

# Define the output file name
outputFile = "output.txt"

# Function to handle key press events
def onKeyPress(key):
    currentTime = time.strftime("%H:%M:%S")

    if hasattr(key, 'char') and key.char is not None:  # Check if key has a char attribute (normal keys)
        char = key.char
    elif key == Key.ctrl_l:  # Handle the special case for Ctrl key
        char = 'CTRL'
    else:
        char = str(key)

    print(f'Press: {char} \t at {currentTime}')

    with open(outputFile, "a+") as file:
        file.write(f'{char} \t at {currentTime}\n')

# Function to handle key release events
def onKeyRelease(key):
    currentTime = time.strftime("%H:%M:%S")

    if hasattr(key, 'char') and key.char is not None:  # Check if key has a char attribute (normal keys)
        char = key.char
    elif key == Key.ctrl_l:  # Handle the special case for Ctrl key
        char = 'CTRL'
    else:
        char = str(key)

    print(f'Release: {char}')
    if key == Key.esc:
        return False

# Set up listener for keyboard events
with Listener(on_press=onKeyPress, on_release=onKeyRelease) as listener:
    listener.join()  # Start the listener and wait for events
