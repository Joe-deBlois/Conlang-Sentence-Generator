This is a program to help conlangers by randomly generating words or sentences given some user input. 

app-initialization.py should be run first; it prompts the user to select between options 1 or 2. 

If option 1 is selected, option1.py will automatically run. This program's userface is through tkinter. 
The user will select IPA characters they want in their words, and the frequency of those sounds. 
They will also develop legal syllable structures, and the phoneme frequencies will be used to set frequencies to each syllable. 
Then the user will specify the number of words desired and the maximum and minimum length of any word. 
Finally the program will output a plaintext file of randomly generated words following these guidelines. 

If option 2 is selected, option2.py will automatically run. 
All the user has to do for this program is input words or a sentence from their conlang. The program specifies some rules on how these words should be inputted. 
The program begins by gathering data on the inputted string's phonemes (e.g. manner of articulation and counts) and syllables (in IPA form and C/V form). 
Next the words are run though a morfessor basic model for morphological segmentation. 
Next...? 
