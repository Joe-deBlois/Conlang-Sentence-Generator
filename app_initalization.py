import subprocess
import sys

while True: 
    option = input("Are you here to \n1) Create conlang sentences from scratch, or \n2) Extrapolate conlang sentences from some input? \nYour choice here: ")
    print(option)
    if option not in ["1", "2"]:
        print ("Option not valid. Please try again.")
    if option == "1":
        print("Beginning option 1")
        subprocess.run(["python", r"C:\Users\Joe deBlois\Desktop\option1.py"])
        sys.exit()  # Ensure the script exits after launching option2
    if option == "2":
        print("Beginning option 2\n\n")
        subprocess.run(["python", r"C:\Users\Joe deBlois\Desktop\option2.py"])
        sys.exit()  # Ensure the script exits after launching option2
