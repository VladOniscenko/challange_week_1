def rock_paper_scissors(game_mode, user_name) -> bool:
    attempts_per_game_mode = {
        'easy': 3,
        'medium': 2,
        'hard': 1
    }

    attempts = attempts_per_game_mode[game_mode]
    print(f'{user_name} you only have to beat me once. If you succeed, you will win this mini-game.')
    print(f'U will have {attempts} attempts.')

    # todo while i < attempts
    # todo get user selection
    # todo generate own selection
    # todo check if user beats us
    # todo return the result of the game

    return False