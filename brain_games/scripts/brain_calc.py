from ..engine import run_game
from ..games.brain_calc import GAME_DESCRIPTION, generate_round


def main():
    run_game(generate_round, GAME_DESCRIPTION)


if __name__ == '__main__':
    main()