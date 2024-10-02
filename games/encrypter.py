# encryption HEX
def encrypter(game_mode) -> bool:
    hex_easy_options = {"YOU": "19-F-15"}

    hex_medium_options = {"I": "9",
                          "SEE":"13-5-5",
                          "YOU":"19-F-15"}

    hex_hard_options = {"YOUR": "19-F-15-12",
                        "DATA": "4-1-14-1",
                        "IS": "9-13",
                        "MINE":"D-9-E-5"}
    hex_options = {
        'easy': hex_easy_options,
        'medium':hex_medium_options,
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
