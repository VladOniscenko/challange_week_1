# encryption HEX
dificulty = 'easy'
hex_easy_options = {"YOU": "19-F-15"}
hex_hard_options = {"HERE": "28-F-32-S",
                    "THERE": "23-SD-32-33-23"}
hex_options = {
    'easy': hex_easy_options,
    'hard': hex_hard_options

}

for x, y in hex_options[dificulty].items():
    answer = input("vul de geïncrypte antwoord in \n")
    if answer.upper() == x:
        print("Yup")