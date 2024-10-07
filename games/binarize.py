# translate binary to digit

import random
def binarize(game_mode) -> bool:
    bin_easy = {'numbers': [["0101", "1111"], ["1010", "1101"], ["0100", "1011"]]}
    bin_medium = {'numbers': [["11111", "011011", "10110"], ["100111", "101101", "111101"],
                              ["101010", "101111", "100011"]]}
    bin_hard = {'numbers': [["1010111", "0111011", "1000110", "1001110"], ["1110110", "1101101", "1111010", "1101111"],
                            ["1111110", "1011010", "1110001", "1000000"]]}

    binarize_modes = {
        'easy': bin_easy,
        'medium': bin_medium,
        'hard': bin_hard
    }

    attempts = 3



    for binary in random.choice(binarize_modes[game_mode]['numbers']):
        print("translate the binary, quickly!")
        print(binary)

        while attempts > 0:
            guess = input("what is the translation?\n")
            if not guess.isdigit():
                print("The answer has to be a number")
            elif int(guess) == int(binary, 2):
                print("Correct!")
                break
            else:
                attempts -= 1
                print(f"incorrect answer, you only have {attempts} tries left...")


        if attempts <= 0:
            print("you failed, good luck ever getting that password")
            return False

    print("you made it!")
    return True





