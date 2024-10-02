import random

red = '\033[91m'
reset = '\033[0m'
green = '\033[92m'
yellow = '\033[93m'

def galgje(game_mode) -> bool:
    correct_chars = []
    incorrect_chars = []

    # check if all character are guessed / return true/false || win/or not yet
    def user_guessed(word, correct_chars):
        for i in word:
            if i == "" or i.isspace():
                continue
            elif i not in correct_chars:
                return False
        return True

    # prints the word boxes in terminal
    def print_ans(word, correct_chars):
        frow, srow, throw = [], [], []

        for letter in word:
            frow.append('+' + '---' + '+ ')

        for letter in word:
            if letter not in correct_chars:
                if letter == "" or letter.isspace():
                    letter = '-'
                else:
                    letter = '?'

            srow.append('| ' + letter + ' | ')

        for letter in word:
            throw.append('+' + '---' + '+ ')

        print(''.join(frow))
        print(''.join(srow))
        print(''.join(throw))

    attempts = 8
    i = 0

    # Galgje game modes
    galgje_modes = {
        'easy': {
            'words': ['cat', 'dog', 'hat', 'sun', 'ball'],
        },
        'medium': {
            'words': ['jungle', 'monkey', 'puzzle', 'bridge', 'shadow'],
        },
        'hard': {
            'words': ['pneumonia', 'subterranean', 'juxtaposition', 'xylophone', 'quizzical'],
        }
    }

    # Get a random word from the selected game mode
    word = random.choice(galgje_modes[game_mode]['words'])

    print_ans(word, correct_chars)

    # while loop until attempts smaller then i
    while i < attempts:
        i += 1
        if user_guessed(word, correct_chars):
            print_ans(word, correct_chars)
            print(f'{green}U guessed it! Word: {word}{reset}')
            break

        # while loop until I get valid input
        while True:
            letter = input("Fill an letter in: ")
            if letter.isalpha() and len(letter) == 1:
                letter = letter.lower()
                break
            else:
                print(f'{red}Input error{reset}')

        # check if character already was used and is in the word or not in it
        if letter in word:
            if letter in correct_chars:
                print(letter + " already guessed!")
                i -= 1
            else:
                print(f'{green}{letter} is in word!{reset}')
                correct_chars.append(letter)
        else:
            if letter in incorrect_chars:
                print(f"Letter {letter} was already used!")
            else:
                incorrect_chars.append(letter)
                print(f"{red}AHH, {letter} is not in the word!{reset}")

        # print attempt results
        print_ans(word, correct_chars)


    # display game results
    if user_guessed(word, correct_chars):
        return True
    else:
        print(f'{yellow}The word was {word}{yellow}')
    return False

if __name__ == '__main__':
    galgje('easy')