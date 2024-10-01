# import sleep to show output for some time period
from time import sleep
import csv

# import mini games
from games.galgje import galgje
from games.math_champ import math_champ
from games.rock_paper_scissors import rock_paper_scissors

def save_score(score):
    time = '9:54'

    # Open the file in append mode and write the data
    with open('scoreboard.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([USER_NAME, score, time])


# printing rules of the game in console
def print_rules() -> None:
    print('Here come the rules of the game')


# greeting the user
def greet_user() -> None:
    print(f"Hello {USER_NAME}!")
    sleep(2)

    print('\nDo you want to play a game? :} ')
    want_to_play = input('yes or no: ').lower()

    sleep(2)

    if want_to_play == 'yes':
        print('\nWell let\'s play then!')
    else:
        print('\nNo one cares what u want!')


# checking if selected action is valid
def validate_action(action: str) -> bool:
    if action.isdigit() and int(action) in [1, 2, 3]:
        return True
    return False


# checking if selected game mode is valid
def validate_game_mode(game_mode: str) -> bool:
    if game_mode.isdigit() and int(game_mode) in [1, 2, 3]:
        return True
    return False


# checking if selected game is not already played and is valid
def validate_selected_game(game_names, game_number) -> bool:

    if not game_number.isdigit() or len(game_names) < int(game_number) - 1 or not game_names[int(game_number) - 1]:
        return False

    selected_game = game_names[int(game_number) - 1]
    if selected_game in played_games:
        return False

    return True


# ask user his name and return to main
def get_user_name() -> str:
    return input("Enter your name: ").strip()

# printing the scoreboard
def print_scoreboard() -> None:
    print_heading('Scoreboard: ')
    with open('scoreboard.csv', mode='r') as file:
        # Read the data into a list and skip the header
        data = list(csv.reader(file))

    # Sort the data by score (second column), converting scores to integers
    sorted_data = sorted(data, key=lambda x: int(x[1]), reverse=True)

    # Print table header
    print(f"{'Name':<15} {'Score':<10} {'Time':<10}")
    print("-" * 35)

    # Print each row in a formatted way
    for row in sorted_data:
        print(f"{row[0]:<15} {row[1]:<10} {row[2]:<10}")

# ask user for preferred game mode [easy, medium, hard]
def get_game_mode() -> str:
    print_heading('Select your game mode: (1 - 3)')
    print('1: Easy')
    print('2: Medium')
    print('3: Hard')

    game_mode = input('\nEnter your game mode: ')
    if not validate_action(game_mode):
        print('Input error')
        return get_game_mode()
    return GAME_MODES[int(game_mode)].lower()


# ask user for the mini-game that he want to play
def get_mini_game():
    print_heading(f'Pick an mini game: (1 - {len(MINI_GAMES)})')
    game_names = []

    i = 1
    for game_name in MINI_GAMES:
        if game_name in played_games:
            print(f'\033[91m{i}: {MINI_GAMES[game_name]["name"]}\033[0m')
        else:
            print(f'{i}: {MINI_GAMES[game_name]["name"]}')

        game_names.append(game_name)
        i += 1

    game_number = input('\nEnter your choice: ')
    if not validate_selected_game(game_names, game_number):
        print('Input error')
        return get_mini_game()

    played_games.append(game_names[int(game_number) - 1])
    return MINI_GAMES[game_names[int(game_number) - 1]]['game']


# ask user what he want to do next
def get_action() -> int:
    print_heading('Make an decision: (1 - 3)')
    print('1: Start new game')
    print('2: See scoreboard')
    print('3: Quit')

    action = input('\nEnter your choice: ')
    if not validate_action(action):
        print('Input error')
        return get_action()

    return int(action)

def get_score(games_won: int) -> int:
    return games_won * 250

# play game binarize
def play_binarize(game_mode) -> bool:
    print_game_rules('binarize')
    return False


# play game rock, paper and scissors
def play_rock_paper_scissors(game_mode) -> bool:
    print_game_rules('rock_paper_scissors')
    if rock_paper_scissors(game_mode, USER_NAME):
        print('\nHmm, you got me this time, it will not happen again!')
        print('Here is your letter: X')
        print('Don\'t forget it :}')
        sleep(2)
        return True
    else:
        sleep(1)
    return False


# play game encrypter
def play_encrypter(game_mode) -> bool:
    print_game_rules('encrypter')
    return False

# plat game galley
def play_galley(game_mode) -> bool:
    print_game_rules('galley')
    if galgje(game_mode):
        print('\nHmm, you got me this time, it will not happen again!')
        print('Here is your letter: X')
        print('Don\'t forget it :}')
        sleep(2)
        return True
    else:
        sleep(1)
    return False

# plat game math champ
def play_math_champ(game_mode) -> bool:
    print_game_rules('math_champ')
    if math_champ(game_mode):
        print('\nHmm, you got me this time, it will not happen again!')
        print('Here is your letter: X')
        print('Don\'t forget it :}')
        sleep(2)
        return True
    else:
        sleep(1)
    return False


# prints the heading in selected color
def print_heading(heading) -> None:
    print(f'\n\033[95m{heading}\033[0m')


def print_game_rules(game_name) -> None:
    print(f'\033[93m{MINI_GAMES[game_name]["rules"]}\033[0m')

    sleep(4)
    print("\nLets start the game :)")
    sleep(1)


# processing the game end
def end_game() -> None:
    pass


# processing the gameplay
def start_game(game_mode) -> int:
    # total score gained while playing
    total_score = 0

    while True:
        if len(played_games) == len(MINI_GAMES):
            break

        # let the user select an mini game
        mini_game = get_mini_game()

        # let user play the game
        user_won = mini_game(game_mode)

        if user_won:
            print(f'\033[92mU won mini-game, this time!\033[0m')
            total_score += 1
        else:
            print(f'\033[91mU lost this mini-game!\033[0m')

    return total_score

def enter_password() -> None:
    pass

if __name__ == '__main__':
    # all game-modes that we support
    GAME_MODES = {
        1: 'Easy',
        2: 'Medium',
        3: 'Hard'
    }

    # all mini-games that we have
    MINI_GAMES = {
        'binarize': {
            'name': 'Binarize',
            'game': play_binarize,
            'rules': 'In Binarize, you are tasked with converting decimal numbers into binary. \n'
                     'You will be given random decimal numbers, and your job is to accurately convert \n'
                     'them to their binary equivalents. Test your knowledge of binary conversions\n'
        },
        'encrypter': {
            'name': 'Encrypter',
            'game': play_encrypter,
            'rules': 'Encrypter challenges you to decode or encode a given string using a specific encryption method, \n'
                     'like Caesar cipher or a substitution cipher. Your goal is to either crack the encrypted message \n'
                     'or encode a message based on the rules provided. Sharpen your cryptography skills!\n'
        },
        'galley': {
            'name': 'Hangman',
            'game': play_galley,
            'rules': 'The objective is to guess a hidden word by suggesting letters. \n'
                     'Each incorrect guess brings the stickman closer to being "hanged." You must guess the word before the man \n'
                     'is fully drawn. It’s a fun word-guessing game that tests your vocabulary and strategic thinking!\n'
        },
        'math_champ': {
            'name': 'Math Champ',
            'game': play_math_champ,
            'rules': 'In Math Champ, you will face equations like A + A = 4 or B + A = 7. Your task is to deduce the values \n'
                     'of the variables (A, B, etc.) by solving these equations. The game will challenge your logical thinking \n'
                     'and problem-solving skills as you figure out the correct values for the variables!\n'

        },
        'rock_paper_scissors': {
            'name': 'Rock Paper Scissors',
            'game': play_rock_paper_scissors,
            'rules': 'Rock Paper Scissors is a classic game of chance where you play against the computer. \n'
                     'Choose rock, paper, or scissors and see if you can outwit the computer. Rock beats scissors, \n'
                     'scissors beats paper, and paper beats rock. Win the best of three rounds to claim victory!\n'
        }
    }

    USER_NAME = get_user_name()
    while True:
        played_games = []
        action = get_action()

        sleep(1)

        if action == 3:
            print('\033[91mWe know that u are scared!\033[0m')
            sleep(2)
            print('\033[91mDon\'t worry we will get you next time! ;}\033[0m')
            exit()

        elif action == 2:
            print_scoreboard()
        elif action == 1:
            # ask for game mode easy, medium or hard
            game_mode = get_game_mode()
            sleep(1)

            greet_user()
            sleep(2)
            print_rules()

            games_won = start_game(game_mode)
            score = get_score(games_won)

            save_user_score = save_score(score)

            get_password = enter_password()
            end_game()
        else:
            continue