import os

from typing import List

from utils.screen import Screen
from utils.status_bar import status_bar

"""
.........
. .. .. .
.........
.........
. .. .. .
.........


.........
.@..    .
. .. .. .
. .. .. .
.    .. .
....... .

.........
. .. .. .
.........
.........
. .. .. .
.........


.........
.@..    .
. .. .. .
. .. .. .
.    .. .
....... .


╭───────────╮
│█@█   *████│
│█ █ ███████│
│█         █│
│██████ ██ █│
│█#     ██ █│
╰───────────╯
╭───────────╮
│███████████│
│███████████│
│███████████│
│███████████│
│███████████│
╰───────────╯

map = {
    "0": (" ", "space", True),
    "1": ("█", name, True),
    "2": ("@", name, False),
    "3": ("*", name, True),
    "4": ("#", name, False),
    "5": ("&", name, False),
}


    # "horizontal": '─',
    # "vertical": '│',
    # "tr": '╮',
    # "tl": '╭',
    # "br": '╯',
    # "bl": '╰',
"""


class Maze:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        s = f'{self.data}'
        return s
    

class DrawingCell:
    def __init__(self, symbol, passable: bool=False):
        self.symbol = symbol
        self.solid = passable

    def __str__(self):
        s = f'{self.symbol}'
        return s
    

class Box:
    def __init__(self, data: List[List[DrawingCell]]):
        self.data = data

        
        self.config = {
            "tl": DrawingCell('╭'),
            "horizontal": DrawingCell('─'),
            "tr": DrawingCell('╮'),
            "vertical": DrawingCell('│'),
            "bl": DrawingCell('╰'),
            "br": DrawingCell('╯'),
            "fallback": DrawingCell('.')
        }

    def __str__(self):
        check_active = lambda x: x[0] if x[2] else x[1]
        
        aa = check_active(self.config.get('aa', '.'))
        ab = check_active(self.config.get('ab', '.'))
        ac = check_active(self.config.get('ac', '.'))
        ba = check_active(self.config.get('ba', '.'))
        bb = check_active(self.config.get('bb', '.'))
        bc = check_active(self.config.get('bc', '.'))
        ca = check_active(self.config.get('ca', '.'))
        cb = check_active(self.config.get('cb', '.'))
        cc = check_active(self.config.get('cc', '.'))


        # "\n".join("".join([ba, *row, bc]) for row in self.split_data)

        s = f'''{aa}{ab}{ac}
{ba}{bb}{bc}
{ca}{cb}{cc}'''
        return s
    
    

def game_loop(width: int=20, height: int=10):
    game_screen = Screen(width=width, height=height, debug=False)    
    while True:
        os.system("cls")
        print(game_screen)
        user_input = input(">>> ")

        match user_input:
            case "q":
                break
            case _:
                game_screen.add_string(user_input, 0, height - 1)
                # input("Invalid Input")

    return



if __name__ == "__main__":
    # Set Screen Width, Height
    # width, height = os.get_terminal_size()
    # SCREEN_WIDTH = width - 2
    # SCREEN_HEIGHT = height - 3

    # game_loop()
    # game_loop(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    SAMPLE_MAZE = f""

    new_cell = Cell("@")
    print(new_cell)




















