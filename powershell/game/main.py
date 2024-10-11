import os

from utils.game import Game


if __name__ == "__main__":
    width, height = os.get_terminal_size()
    SCREEN_WIDTH, SCREEN_HEIGHT = width - 2, height -3

    new_game = Game(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    new_game.run()

