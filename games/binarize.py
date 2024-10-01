# translate binary to digit
def binarize(game_mode) -> bool:
    bin_easy = {'numbers': ["0101", "1111"]}
    bin_medium = {'numbers': ["11111", "011011", "1000110"]}
    bin_hard = {'numbers': ["11111", "011011", "1000110", "10011101"]}

    binarize_modes = {
        'easy': bin_easy,
        'medium': bin_medium,
        'hard': bin_hard
    }

    attempts = 3



    for binary in binarize_modes[game_mode]['numbers']:
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
                print(f"incorrect answer, you only have {attempts} tries left...")

        if attempts <= 0:
            print("you failed, good luck ever getting that password")
            return False

    print("you made it!")
    return True





