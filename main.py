from boggle import BoggleBoard

def main():
    game = BoggleBoard(9999)
    game.create_board()
    game.print_board()
    word = input('Enter word (in UPPERcase): ')
    game.guess_word(word)


main()