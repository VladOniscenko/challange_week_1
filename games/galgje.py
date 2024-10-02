def galgje(game_mode) -> bool:
    correct_chars, incorrect_chars = [], []

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

    attempts = 7
    i = 0

    import random
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[94m'
    reset = '\033[0m'
    green = '\033[92m'
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
        if user_guessed(word, correct_chars):
            print_ans(f'{green}U guessed it! Word: {word}{reset}')
            break

        attempt_number = i + 1

        # while loop until I get valid input
        while True:
            attempt = input("Attempt " + str(attempt_number) + ": ")
            if not attempt:
                attempt = input("Attempt " + str(attempt_number) + ": ")
            else:
                attempt = attempt[0].lower()
                break

        # check if character already was used and is in the word or not in it
        if attempt in word:
            if attempt in correct_chars:
                print(attempt + " already guessed!")
                i = i - 1
            else:
                print(f'{green}{attempt} is in word!{reset}')
                correct_chars.append(attempt)
        else:

            if attempt in incorrect_chars:
                print(attempt + " was already used!")
            else:
                incorrect_chars.append(attempt)
                print(f"{red}AHH, " + attempt + f" is not in the word!{reset}")
                i += 1
        # print attempt results
        print_ans(word, correct_chars)


    # display game results
    if user_guessed(word, correct_chars):
        return True
    return False

if __name__ == '__main__':
    galgje('easy')