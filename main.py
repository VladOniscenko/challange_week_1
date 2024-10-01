# import sleep to show output for some time period
from time import sleep


# import mini games
from games.galgje import galgje
from games.math_champ import math_champ
from games.rock_paper_scissors import rock_paper_scissors


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
    print('Here comes the scoreboard')

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
    # todo print here the rules of each game

    sleep(1)
    print("\nLets start the game :)")
    sleep(2)


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
            total_score += 1

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
        },
        'encrypter': {
            'name': 'Encrypter',
            'game': play_encrypter,
        },
        'galley': {
            'name': 'Galley',
            'game': play_galley,
        },
        'math_champ': {
            'name': 'Math Champ',
            'game': play_math_champ,
        },
        'rock_paper_scissors': {
            'name': 'Rock Paper Scissors',
            'game': play_rock_paper_scissors,
        }
    }

    USER_NAME = get_user_name()
    while True:
        played_games = []
        action = get_action()

        sleep(1)
        # ask for game mode easy, medium or hard
        game_mode = get_game_mode()
        sleep(1)

        greet_user()
        sleep(2)
        print_rules()

        if action == 3:
            print('\033[91mWe know that u are scared!\033[0m')
            sleep(2)
            print('\033[91mDon\'t worry we will get you next time! ;}\033[0m')
            exit()

        elif action == 2:
            print_scoreboard()
        elif action == 1:
            score = start_game(game_mode)

            print(f'TOTAL SCORE: {score}')
            get_password = enter_password()
            end_game()
        else:
            continue