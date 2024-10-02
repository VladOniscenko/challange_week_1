# import sleep to show output for some time period
from time import sleep, time
import csv

# import mini games
from games.galgje import galgje
from games.math_champ import math_champ
from games.rock_paper_scissors import rock_paper_scissors
from games.encrypter import encrypter
from games.binarize import binarize

def save_score(score: int, time: float, game_mode: str) -> None:
    # Open the file in append mode and write the data
    with open('scoreboard.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([USER_NAME, score, int(time), game_mode])

# printing rules of the game in console
def print_rules():
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[94m'
    reset = '\033[0m'
    green = '\033[92m'

    # Game rules
    rules = (
        f"{red}Game rules:{reset}\n"
        f"{yellow}1. You will play a series of mini-games.{reset}\n"
        f"{yellow}2. For each mini-game, you will earn a letter.{reset}\n"
        f"{yellow}3. If you win the most mini-games, you can decrypt the password in a later stage.{reset}\n"
        f"{yellow}4. There are a total of 5 mini-games.{reset}\n"
    )

    print(rules)


def print_story() -> None:
    red = '\033[91m'
    yellow = '\033[93m'
    blue = '\033[94m'
    reset = '\033[0m'
    green = '\033[92m'

    pre_story = (
        f"{red}WARNING: A malicious entity has infiltrated your computer {USER_NAME}!{reset}\n"
        f"{blue}The Cookie Monster, driven by his hunger for cookies, has spread a virus across your system.{reset}\n"
        f"{red}Your files are at risk, and he demands the ultimate password to unleash his sugary chaos!{reset}\n"
        f"{green}You must fight back by playing games to get letters and decrypt the password.{reset}\n"
        f"{blue}Only then can you save your computer from his cookie-fueled mayhem...{reset}\n"
    )

    enters = ('\n' * 50)
    print(enters)

    # Print the pre-story
    print(pre_story)
    sleep(5)


def print_scary_message() -> None:
    # ANSI escape codes for colors
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    reset = '\033[0m'  # Reset to default color

    # Scary message with styling
    message = (
        f"{red}A dark shadow looms behind you, {yellow}{USER_NAME}{red}...{reset}\n"
        f"{red}Its cold breath whispers your name, but no one is around to hear it.\n"
        f"{green}You turn around, but all you see is darkness...{reset}\n"
        f"{red}Will you face it, {yellow}{USER_NAME}{red}? Or will you run into the night?{reset}"
    )

    print(message)


# greeting the user
def greet_user() -> None:
    print_scary_message()
    sleep(5)

    print(f'\nDo you want to play a game {USER_NAME}? :@ ')
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
    print(f"{'Name':<15} {'Score':<10} {'Time':<10} {'Difficulty':<10}")
    print("-" * 55)

    # Print each row in a formatted way
    for row in sorted_data:
        # Calculate minutes and seconds
        minutes = int(float(row[2]) // 60)
        seconds = int(float(row[2])) % 60

        time = f'{minutes}:{seconds}'
        print(f"{row[0]:<15} {row[1]:<10} {time:<10} {row[3]:<10}")

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
    print_heading(f'Pick an game: (1 - {len(MINI_GAMES)})')
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

def get_score(games_won: int, time: float) -> int:
    # Calculate the score
    score = (games_won * 1000) - (time * 0.1)

    # Ensure the score is non-negative
    return max(0, int(score))

# play game binarize
def play_binarize(game_mode) -> bool:
    print_game_rules('binarize')

    if binarize(game_mode):
        print('\nHmm, you got me this time, it will not happen again!')
        print('Here is your letter: cha')
        print('Don\'t forget it :}')
        sleep(2)
        return True
    else:
        sleep(1)
    return False


# play game rock, paper and scissors
def play_rock_paper_scissors(game_mode) -> bool:
    print_game_rules('rock_paper_scissors')
    if rock_paper_scissors(game_mode, USER_NAME):
        print('\nHmm, you got me this time, it will not happen again!')
        print('Here is your letter: ll')
        print('Don\'t forget it :}')
        sleep(2)
        return True
    else:
        sleep(1)
    return False


# play game encrypter
def play_encrypter(game_mode) -> bool:
    print_game_rules('encrypter')
    if encrypter(game_mode):
        print('\nHmm, you got me this time, it will not happen again!')
        print('Here is your letter: en')
        print('Don\'t forget it :}')
        sleep(2)
        return True
    else:
        sleep(1)


    return False

# plat game galley
def play_galley(game_mode) -> bool:
    print_game_rules('galley')
    if galgje(game_mode):
        print('\nHmm, you got me this time, it will not happen again!')
        print('Here is your letter: g')
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
        print('Here is your letter: e')
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
        enters = ('\n' * 50)
        print(enters)
        user_won = mini_game(game_mode)

        if user_won:
            print(f'\033[92mU won mini-game, this time!\033[0m')
            total_score += 1
        else:
            print(f'\033[91mU lost this mini-game!\033[0m')

    return total_score

def enter_password() -> bool:
    password = input('Enter password: ')
    if password.lower() == 'challenge':
        return True
    return False

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
            'rules': 'Encrypter challenges you to decode a message using a specific encryption method, \n'
                     'The only clue C. Monster has left to decode the message is the following \n'
                     '\"only HEXES will save you, B=2\" \n'
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

    print_rules()
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
            red = '\033[91m'
            yellow = '\033[93m'
            blue = '\033[94m'
            reset = '\033[0m'
            green = '\033[92m'
            # ask for game mode easy, medium or hard
            game_mode = get_game_mode()
            sleep(1)

            print_story()

            # greet user and print rules of the game
            greet_user()
            sleep(2)

            # start timer and game
            start_time = time()
            games_won = start_game(game_mode)

            print_heading("U ALMOST ESCAPED!")
            print_heading("Now u can put all letters together and try to crack the password!")

            if enter_password():
                games_won += 10
                print(f'{green}Password is correct! THE END! {reset}')
            else:
                print(f'{red}Password was incorrect! THE END! {reset}')

            end_time = time()

            # calculate score
            score = get_score(games_won, end_time - start_time)

            # save the score
            save_user_score = save_score(score, end_time - start_time, game_mode)
        else:
            continue