# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

def get_user_name():
    return input("Enter your name: ").strip()


def print_rules():
    print('Here come the rules of the game')


def greet_user():
    print(f"Hello {user_name}!")
    sleep(2)

    print('\nDo you want to play a game? :} ')
    want_to_play = input('yes or no: ').lower()

    sleep(2)

    if want_to_play == 'yes':
        print('\nWell let\'s play then!')
    else:
        print('\nNo one cares what u want!')


def validate_action(action: str) -> bool:
    if action.isdigit() and int(action) in [1, 2, 3]:
        return True
    return False


def validate_game_mode(game_mode: str) -> bool:
    if game_mode.isdigit() and int(game_mode) in [1, 2, 3]:
        return True
    return False


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


def print_scoreboard():
    print('Here comes the scoreboard')


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


def play_binarize():
    print('U are playing Binarize')


def validate_selected_game(game_names, game_number) -> bool:

    if not game_number.isdigit() or len(game_names) < int(game_number) - 1 or not game_names[int(game_number) - 1]:
        return False

    selected_game = game_names[int(game_number) - 1]
    if selected_game in played_games:
        return False

    return True


def print_heading(heading):
    print(f'\n\033[95m{heading}\033[0m')


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


def end_game():
    print('\nU are a noob u lost!')


def start_game():
    # ask for game mode easy, medium or hard
    game_mode = get_game_mode()

    while True:
        if len(played_games) == len(MINI_GAMES):
            break

        # let the user select an mini game
        mini_game = get_mini_game()
        user_won = mini_game()

        if user_won:
            total_score += 1

def play_rock_paper_scissors():
    print('Play rock_paper_scissors')


def play_encrypter():
    print('Play play_encrypter')


def play_galley():
    player_won = False

    print("\nRULES OF THE GAME:")
    print("U have 9 attempts to guess the word.")
    print("If u guess the word correctly within 9 attempts, you get 1 point")
    print("Otherwise U DIE!")
    print("")
    print("")
    print("Lets start the game :)")

    import galgje

    if player_won:
        print('Hmm, you got me this time, it will not happen again!')
        return True
    else:
        print('How do u feel to be an loser?')

        sleep(2)
        print('U are close to die!')
        return False

def play_math_champ():
    print('Play play_math_champ')


if __name__ == '__main__':
    GAME_MODES = {
        1: 'Easy',
        2: 'Medium',
        3: 'Hard'
    }
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

    user_name = get_user_name()
    greet_user()

    sleep(2)
    print_rules()

    sleep(2)
    while True:
        played_games = []
        action = get_action()

        if action == 3:
            print('\033[91mWe know that u are scared!\033[0m')
            sleep(2)
            print('\033[91mDon\'t worry we will get you next time! ;}\033[0m')
            exit()

        elif action == 2:
            print_scoreboard()
        elif action == 1:
            total_score = 0

            start_game()
            end_game()
        else:
            continue