import random
from time import sleep

attempts_per_game_mode = {
    'easy': 3,
    'medium': 2,
    'hard': 1
}

options = ['rock', 'paper', 'scissors']

# play the game
def rock_paper_scissors(game_mode, user_name) -> bool:
    random_option = random.choice(options)

    attempts = attempts_per_game_mode[game_mode]
    print(f'{user_name} you only have to beat me once. If you succeed, you will win this mini-game.')
    print(f'U will have {attempts} attempt(\'s).')
    sleep(2)

    for attempt in range(attempts):
        user_selection = get_rock_paper_scissors()
        print(f'You chose \033[95m{user_selection}\033[0m and I chose \033[95m{random_option}\033[0m.')

        if (user_selection == "rock" and random_option == "scissors") or (user_selection == "paper" and random_option == "rock") or (user_selection == "scissors" and random_option == "paper"):
            print(f'\033[92mU won this time!\033[0m')
            return True
        else:
            print(f'\033[91mU lost this time!\033[0m')
            continue

    return False


# check if inputted selection is valid
def validate_selection(selection) -> bool:
    if selection.isdigit() and int(selection) in [1,2,3]:
        return True
    return False


# ask user for an selection [rock, paper, scissors]
def get_rock_paper_scissors() -> str:
    print_heading('Make an choice: (1 - 3)')
    print('1: Rock')
    print('2: Paper')
    print('3: Scissors')

    selection_str = input('\nMake your choice: ')
    if validate_selection(selection_str):
        selection = int(selection_str)
        return options[selection - 1]

    print('Input error')
    return get_rock_paper_scissors()


# prints the heading in selected color
def print_heading(heading) -> None:
    print(f'\n\033[95m{heading}\033[0m')


if __name__ == '__main__':
    rock_paper_scissors('easy', 'vlad')