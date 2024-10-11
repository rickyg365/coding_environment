import os
import json

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


def save_json(data, filename: str="default_save.json"):
    with open(filename, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return True

def load_json(filename: str="default_save.json"):
    data = None
    with open(filename, 'r') as load_buf:
        data = json.load(load_buf)
    return data


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



    sample_character_data = {
        "id": "00",
        "name": "Blank",
        "level": 0,
        "current_health": 1,
        "max_health": 1,
        "current_mp": 1,
        "max_mp": 1,
        "attack": 1,
        "defense": 1,
        "special_attack": 1,
        "special_defense": 1,
        "speed": 1,
        "luck": 1,
    }
    data = save_json(sample_character_data, "test_character_data.json")

    sample_enemy_character_data = [
        {
            "id": "00",
            "name": "Blank",
            "level": 0,
            "current_health": 1,
            "max_health": 1,
            "current_mp": 1,
            "max_mp": 1,
            "attack": 1,
            "defense": 1,
            "special_attack": 1,
            "special_defense": 1,
            "speed": 1,
            "luck": 1,
        },
        {
            "id": "00",
            "name": "Blank",
            "level": 0,
            "current_health": 1,
            "max_health": 1,
            "current_mp": 1,
            "max_mp": 1,
            "attack": 1,
            "defense": 1,
            "special_attack": 1,
            "special_defense": 1,
            "speed": 1,
            "luck": 1,
        },
        {
            "id": "00",
            "name": "Blank",
            "level": 0,
            "current_health": 1,
            "max_health": 1,
            "current_mp": 1,
            "max_mp": 1,
            "attack": 1,
            "defense": 1,
            "special_attack": 1,
            "special_defense": 1,
            "speed": 1,
            "luck": 1,
        },
        {
            "id": "00",
            "name": "Blank",
            "level": 0,
            "current_health": 1,
            "max_health": 1,
            "current_mp": 1,
            "max_mp": 1,
            "attack": 1,
            "defense": 1,
            "special_attack": 1,
            "special_defense": 1,
            "speed": 1,
            "luck": 1,
        }
    ]
