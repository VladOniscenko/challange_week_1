# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep


#get mini game galgje
from galgje import galgje

# printing rules of the game in console
def print_rules() -> None:
    print('Here come the rules of the game')


# greeting the user
def greet_user() -> None:
    print(f"Hello {user_name}!")
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
def play_binarize() -> bool:
    print('U are playing Binarize')
    return False


# play game rock, paper and scissors
def play_rock_paper_scissors() -> bool:
    print('Play rock_paper_scissors')
    return False


# play game encrypter
def play_encrypter() -> bool:
    print('Play play_encrypter')
    return False

# plat game galley
def play_galley(game_mode) -> bool:
    print("\nRULES OF THE GAME:")
    print("U have 10 attempts to guess the word.")
    print("If u guess the word correctly within 10 attempts, you get 1 point")
    print("Otherwise U DIE!")
    print("")
    print("")
    print("Lets start the game :)")
    sleep(2)

    if galgje(game_mode):
        print('\nHmm, you got me this time, it will not happen again!')
        return True
    else:
        print('\nHow do u feel to be an loser?')

        sleep(1)
        print('U are close to die!')

        sleep(1)
        return False

# plat game math champ
def play_math_champ() -> bool:
    print('Play play_math_champ')
    return False


# prints the heading in selected color
def print_heading(heading) -> None:
    print(f'\n\033[95m{heading}\033[0m')


# processing the game end
def end_game() -> None:
    pass


# processing the gameplay
def start_game() -> None:
    # ask for game mode easy, medium or hard
    game_mode = get_game_mode()

    while True:
        if len(played_games) == len(MINI_GAMES):
            break

        # let the user select an mini game
        mini_game = get_mini_game()

        # let user play the game
        user_won = mini_game(game_mode)

        if user_won:
            total_score += 1


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