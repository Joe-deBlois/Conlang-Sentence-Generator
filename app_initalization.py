import subprocess
import sys
import os

# Get directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))
option1_path = os.path.join(current_dir, 'option1.py')
option2_path = os.path.join(current_dir, 'option2.py')

while True: 
    option = input("Are you here to \n1) Create conlang sentences from scratch, or \n2) Extrapolate conlang sentences from some input? \nYour choice here: ")
    print(option)
    if option not in ["1", "2"]:
        print ("Option not valid. Please try again.")
    if option == "1":
        print("Beginning option 1")
        subprocess.run(['python', option1_path])
        sys.exit()  # Ensure the script exits after launching option2
    if option == "2":
        print("Beginning option 2\n\n")
        subprocess.run(['python', option2_path])
        sys.exit()  # Ensure the script exits after launching option2
