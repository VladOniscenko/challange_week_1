# encryption HEX
def encrypter(game_mode) -> bool:
    hex_easy_options = {"YOU": "19-F-15"}
    hex_hard_options = {"HERE": "28-F-32-S",
                        "THERE": "23-SD-32-33-23"}
    hex_options = {
        'easy': hex_easy_options,
        'hard': hex_hard_options
    }

    attempts = 3

    for answer, question in hex_options[game_mode].items():

        while attempts > 0:
            print(question)
            guess = input("vul het geïncrypte antwoord in \n")
            if not guess.isalpha():
                print("The answer has to be a word")
            elif guess.upper() == answer:
                print("Correct!")
                break
            else:
                attempts -= 1
                print(f"incorrect answer, you only have {attempts} tries left...")
        if attempts <= 0:
            return False

    print("you made it!")
    return True
