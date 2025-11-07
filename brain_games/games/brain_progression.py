import random

GAME_DESCRIPTION = 'What number is missing in the progression?'

MIN_LENGTH = 5
MAX_LENGTH = 10
PLACEHOLDER = '..'


def generate_round():
    start_num = random.randint(1, 20)
    step = random.randint(2, 5)
    progression_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    
    progression = []
    current_num = start_num
    for _ in range(progression_length):
        progression.append(current_num)
        current_num += step
        # вместо current_num = start_num + i * step
    
    hidden_index = random.randint(0, progression_length - 1)

    correct_value = progression[hidden_index]
    correct_answer = str(correct_value)

    progression[hidden_index] = PLACEHOLDER
    question = ' '.join(map(str, progression))

    return question, correct_answer
