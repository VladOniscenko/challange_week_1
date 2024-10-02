import random

# Question difficulties and corresponding number of variables
questions = {
    'easy': 2,
    'medium': 3,
    'hard': 4
}


# Variable values
values = {
    'A': 2,
    'B': 5,
    'C': 7,
    'D': 10,
    'E': 1
}


def generate_equation(game_mode):
    print(f'\nExamples:')
    print(f'A + A = {values["A"] + values["A"]}')
    print(f'B + A = {values["B"] + values["A"]}')
    print(f'B + C = {values["B"] + values["C"]}')
    print(f'C + D = {values["D"] + values["C"]}')
    print(f'D + E = {values["D"] + values["E"]}\n')

    # Choose a number of variables based on game_mode
    num_variables = questions[game_mode]
    chosen_vars = random.sample(list(values.items()), num_variables)

    # Create string
    equation_str = " + ".join([f"{var}" for var, i in chosen_vars])
    equation_result = sum([val for key, val in chosen_vars])

    print(f"Solve: {equation_str} = {equation_result}")
    return {var: val for var, val in chosen_vars}


def math_champ(game_mode):
    # Generate an equation
    equation_vars = generate_equation(game_mode)

    # Get user's guesses
    user_guesses = {}
    for var in equation_vars:
        while True:
            guess = input(f"What is the value of {var}? ")
            if guess.isdigit():
                guess = int(guess)
                break
            print("Input error")
        user_guesses[var] = guess

    # Check if the user's guesses are correct
    user_won = bool(user_guesses == equation_vars)

    if user_won:
        print(f'\033[92mU got it this time!\033[0m')
        return True
    else:
        print(f'\033[91mU lost this time!\033[0m')

    return user_won


if __name__ == "__main__":
    math_champ('easy')