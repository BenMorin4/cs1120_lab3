# Project No.: 3
# Author: Trent Kimmel & Ben Morin
# Description: Project creates a simulation of the board game Boggle by creating a 4x4 square based of a input seed,
# asks user to chain together a word present on the board, and checks if word is valid as well as if word in palindrome.



from boggle import (BoggleBoard)

def main():
    seed = int(input("Enter the seed: ")) # Prompt the user to enter the seed for randomization
    game = BoggleBoard(seed)  # Create an instance of the BoggleBoard class with the specified seed
    game.print_board()  # Print the initial Boggle board

    while True:
        word = input ("Enter word (in UPPERcase) or 'quit' to exit: ").upper()  # Prompt the user to enter a word or 'quit' to exit
        if word == 'QUIT':
            break  # Exit the loop if the user inputs 'quit'
        game.guess_word(word) # Attempt to find the entered word on the Boggle board


if __name__ == "__main__":
    main()
