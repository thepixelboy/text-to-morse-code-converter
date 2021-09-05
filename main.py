import os

# Morse Code Dictionary
MORSE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "_",
}

# Global variables
turn_off = False

# Morse Code Converter funcion
def convert_to_morse_code(sentence):
    """Converts a sentence to morse code"""
    converted_sentence = ""

    for letter in sentence:
        converted_sentence += MORSE_DICT[letter] + " "

    return converted_sentence


def clrscr():
    """Clears the screen"""
    # Check if Operating System is Mac and Linux or Windows
    if os.name == "posix":
        _ = os.system("clear")
    else:
        # Else Operating System is Windows (os.name = nt)
        _ = os.system("cls")


# Main program
clrscr()

while not turn_off:
    sentence = input("Enter a sentence to convert-it to Morse Code (off. to exit program): ")

    if sentence == ("off."):
        turn_off = True
        clrscr()
    else:
        print(f"Your translated sentence: {convert_to_morse_code(sentence.upper())}\r\n")
