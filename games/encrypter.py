# encryption HEX
import random
def encrypter(game_mode) -> bool:
    hex_easy_options = [{"YOU": "19-F-15"}, {"MINE":"D-9-E-5"}, {"DATA":"4-1-14-1"}]

    hex_medium_options = [{"I": "9",
                          "SEE":"13-5-5",
                          "YOU":"19-F-15"},
                          {"NOT":"E-F-14",
                           "ENOUGH":"5-E-F-15-7-8",
                           "TIME":"14-9-D-5"},
                          {"NOT":"E-F-14",
                           "SAFE":"13-1-6-5",
                           "HERE":"8-13-12"}]

    hex_hard_options = [{"YOUR": "19-F-15-12",
                        "DATA": "4-1-14-1",
                        "IS": "9-13",
                        "MINE":"D-9-E-5"},
                        {"TIME":"",
                         "IS":"",
                         "RUNNING":"",
                         "OUT":""},
                        {"QUIT":"11-15-9-14",
                         "WHILE":"17-8-9-5",
                         "YOU":"19-F-15",
                         "CAN":"3-1-E"}]
    hex_options = {
        'easy': hex_easy_options,
        'medium':hex_medium_options,
        'hard': hex_hard_options
    }

    attempts = 3

    for answer, question in random.choice(hex_options[game_mode]).items():

        while attempts > 0:
            print(question)
            guess = input("Fill in the decrypted word \n")
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
