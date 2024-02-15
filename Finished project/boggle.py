# Project No.: 3
# Author: Trent Kimmel & Ben Morin
# Description: Project creates a simulation of the board game Boggle by creating a 4x4 square based of a input seed,
# asks user to chain together a word present on the board, and checks if word is valid as well as if word in palindrome.

import string
import random


class BoggleBoard:
# Initialize the BoggleBoard with a seed for random letter generation.
    def __init__(self, seed):
        self.__seed = seed
        self.create_board()

# Getter and setter methods for the class attributes
    def set_seed(self, seed):
        self.__seed = seed

    def get_seed(self):
        return self.__seed

    def set_board(self, board):
        self.__board = board

    def get_board(self):
        return self.__board

    # Create the BoggleBoard using the seed given
    def create_board(self):
        random.seed(self.__seed) 
        self.__board = [[random.choice(string.ascii_uppercase) for _ in range(4)] for _ in range(4)]

    # Print the BoggleBoard, highlighting word if valid.
    def print_board(self, highlighted_path=None):
        print("+---+ " * 4)  
        for row_index, row in enumerate(self.__board):
            for col_index, char in enumerate(row): 
                # Highlight letters that are part of the guessed word path.
                format_char = f"<{char}>" if highlighted_path and (
                row_index, col_index) in highlighted_path else f" {char} "
                print(f'|{format_char}|', end=' ')
            print("\n" + "+---+ " * 4)  

    # Checks if users word is valid
    def guess_word(self, word):
        if not word: 
            return
        word = word.upper()  
        path = self.__find_word_path(word)  
        # Determine the message based on whether a path was found.
        message = "Nice Job!" if path else "I don't see that word."
        message2 = "Are we looking at the same board?"
        self.__print_result(word, path, message, message2)

    # Recursive method to find if the word exists on the board.
    def __find_word_path(self, word, row=0, col=0, visited=set(), path=[]):
        if not word:  # Base case
            return path
        if path:  # Determine next positions based on the last letter found.
            starting_points = [(path[-1][0] + dx, path[-1][1] + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
        else:  
            starting_points = [(x, y) for x in range(4) for y in range(4)]

        for dx, dy in starting_points:
            if 0 <= dx < 4 and 0 <= dy < 4 and (dx, dy) not in visited and self.__board[dx][dy] == word[0]:
                next_visited = visited.copy()
                next_visited.add((dx, dy))
                next_path = path + [(dx, dy)]
                if len(word) == 1:
                    return next_path  
                result = self.__find_word_path(word[1:], dx, dy, next_visited, next_path)
                if result:
                    return result  
        return None  # Return None if the word cannot be formed.

    # Check if the word is a palindrome.
    def __print_result(self, word, path, message, message2):
        print(message)
        print(f"The word {word} is {'a palindrome.' if self.__is_palindrome(word) else 'not a palindrome.'}")
        if not path:
            print(message2)
        if path:
            self.print_board(path)  # Reprint the board with the path highlighted.

    # Recursive method to check if the given word is a palindrome.
    def __is_palindrome(self, word):
        if len(word) <=1:  # Base case
            return True
        elif word[0] == word[-1]:    # Passes in the next 2 closest letters in the word
            return self.__is_palindrome(word[1:-1])
