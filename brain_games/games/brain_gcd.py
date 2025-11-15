import random

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        temp = b
        b = a % b
        a = temp
    return a


def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 20)

    question = f"{num1} {num2}"

    result = gcd(num1, num2)

    correct_answer = str(result)

    return question, correct_answer