import os

from utils.screen import Screen
from utils.object import Object
from utils.character import Character

from utils.text_block import TextBlock


"""
█


╭─╮
│ │
╰─╯

┌─┐
│ │
└─┘
├ ┤ ┬ ┴ ┼

┏━┓
┃ ┃
┗━┛
┣ ┫ ┻ ┳ ╋


╔═╗
║ ║
╚═╝
╠   ╣	╦	╩	╬


╴	╵	╶	╷	
╸	╹	╺	╻	

"""



class Game:
    def __init__(self, width: int=0, height: int=0):
        self.width = width
        self.height = height

        self.screen = Screen(width=width, height=height, debug=False)

    
    def __str__(self):
        s = f'{self.width}'
        return s
    
    def run(self):
        main_char = Character("Hero", level=1)
        enemy = Character("Goblin", level=1)
        char_txt = TextBlock(str(main_char), border=True)
        enemy_txt = TextBlock(str(enemy), border=True)

        # print(self.width - char_txt.width - 2, self.height - char_txt.height - 2)
        # print(f"{char_txt}")
        # input()

        self.screen.add_string_block(f"{char_txt}", self.width - char_txt.width - 2, self.height - char_txt.height - 2)  # 51, 23
        self.screen.add_string_block(f"{enemy_txt}", 0, 0)  # 51, 23
        while True:
            os.system("cls")
            print(self.screen)
            user_input = input(">>> ")

            match user_input:
                case "q":
                    break
                case _:
                    self.screen.add_string(user_input, 0, self.height - 1)
                    # input("Invalid Input")
    



if __name__ == "__main__":
    # Set Screen Width, Height
    width, height = os.get_terminal_size()
    SCREEN_WIDTH = width - 2
    SCREEN_HEIGHT = height - 3

    # main_screen = Screen(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    # print(main_screen)

    Game(width=SCREEN_WIDTH, height=SCREEN_HEIGHT).run()
