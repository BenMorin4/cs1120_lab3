import string
import random

class BoggleBoard():
    def __init__(self, seed):
        self.__seed = seed

    def set_seed(self, seed):
        self.__seed = seed

    def get_seed(self):
        return self.__seed
    
    def set_board(self, board):
        self.__board = board

    def get_board(self):
        return self.__board
    
    def create_board(self):
        random.seed(self.__seed)
        self.__board = [[0,0,0,0] for _ in range(4)]

        for row in range(4):
            for col in range(4):
                self.__board[row][col] = random.choice(string.ascii_uppercase)
        
    def print_board(self):
        for row in self.__board:
            self.__print_box_line()
            self.__print_box_characters(row)
            self.__print_box_line()

    def __print_box_line(self):
        for _ in range(4):
            print("+---+ ", end='')
        print()

    def __print_box_characters(self, chars):
        for char in chars:
            print(f'| {char} | ', end='')
        print()

    def guess_word(self, word):
        # call function to find the first letter then perform recursive step
        self.__find_word(word)

    def __find_word(self, word):
        for row in self.__board:
            for char in self.__board:
                if word[0] == char:
                    # found first letter, start recursive function

    def __follow_word(word):
