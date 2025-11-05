MAX_ROUNDS = 3


def get_username():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    return user_name


def run_game(generate_round_function, game_description):
    user_name = get_username() 
    print(game_description)

    correct_count = 0

    while correct_count < MAX_ROUNDS:
        question, correct_answer = generate_round_function()
        
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return 
            
    print(f"Congratulations, {user_name}!")