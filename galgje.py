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


attempts = 5
i = 0

# while loop until I get valid input
word = "vlad"

print_ans(word, correct_chars)

# while loop until attempts smaller then i
while i < attempts:
    if user_guessed(word, correct_chars):
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
            print(attempt + " is in word!")
            correct_chars.append(attempt)
    else:

        if attempt in incorrect_chars:
            i = i - 1
            print(attempt + " was already used!")
        else:
            incorrect_chars.append(attempt)
            print("AHH, " + attempt + " is not in the word!")

    # print attempt results
    print_ans(word, correct_chars)

    i += 1

# display game results
if user_guessed(word, correct_chars):
    player_won = True
else:
    player_won = False




