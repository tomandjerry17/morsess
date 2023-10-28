import random
print("--------------------------------------------")
print("**************** Title Here ****************")
print("--------------------------------------------")


def rerun():  # Handle rerun function

    choice1 = input("\nWould you like to play again Y|N?\n>> ")

    if choice1 == "Y" or choice1 == "y":
        print(morseCode())
    elif choice1 == "N" or choice1 == "n":
        print("Okay! see you next time!")
    else:
        print("That is invalid!", rerun())
    return " "


def morseCode():  # Main code, Handles the main point of the program

    # Define Morse code patterns and their corresponding letters
    morse_codes = {".-": 'a', "-...": 'b', "-.-.": 'c', "-..": 'd', ".": 'e', "..-.": 'f', "--.": 'g', "....": 'h', "..": 'i', ".---": 'j', "-.-": 'k', ".-..": 'l', "--": 'm', "-.": 'n', "---": 'o', ".--.": 'p', "--.-": 'q', ".-.": 'r', "...": 's', "-": 't', "..-": 'u', "...-": 'v', ".--": 'w', "-..-": 'x', "-.--": 'y', "--..": 'z'}

    # Randomly select a Morse code pattern
    random_morse = random.choice(list(morse_codes.keys()))

    # Print a message to the user
    print("\nGuess the letter for the following Morse code:\n")
    print("\t", random_morse)

    # Get user input
    user_input = input("Enter your guess:\n>> ")

    # Check if the user's input matches the correct answer
    correct_answer = morse_codes[random_morse]

    if user_input == correct_answer:
        print("Nice! You guessed it correctly.")
        rerun()
    else:
        print(f"Wrong. The correct answer is '{correct_answer}'\n")
        rerun()

        return" "


morseCode()
