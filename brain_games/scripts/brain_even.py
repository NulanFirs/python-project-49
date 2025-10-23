import random


def get_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


def run_brain_even():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")

    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_count = 0
    MAX_ROUNDS = 3
    
    while correct_count < MAX_ROUNDS:
        number = random.randint(1, 100)
        
        correct_answer = get_correct_answer(number)
        
        print(f"Question: {number}")
        user_answer = input("Your answer: ")
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")


def main():
    run_brain_even()


if __name__ == "__main__":
    main()
