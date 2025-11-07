import random

GAME_DESCRIPTION = ('Answer "yes" if given number is prime. '
    'Otherwise answer "no".')


def is_prime(number):
    if number <= 1:
        return False
    
    if number == 2:
        return True
        
    if number % 2 == 0:
        return False
    
    i = 3
    while i * i <= number: 
        if number % i == 0:
            return False
        i += 2
        
    return True


def generate_round():
    number = random.randint(1, 100)

    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = str(number)

    return question, correct_answer
