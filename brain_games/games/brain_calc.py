import random

GAME_DESCRIPTION = 'What is the result of the expression?'


def generate_round():

    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    operator = random.choice(['+', '-', '*'])
    
    question = f'{num1} {operator} {num2}'

    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case _:
            raise ValueError("Invalid operator")
    
    correct_answer = str(result)

    return question, correct_answer
