import os
import json
import random

from utils.text_block import TextBlock
from utils.screen import Screen
from utils.character import Character, HeroTypes


def save_json(data, filename: str="default_save.json"):
    with open(filename, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return True

def load_json(filename: str="default_save.json"):
    data = None
    with open(filename, 'r') as load_buf:
        data = json.load(load_buf)
    return data


SAMPLE_CHARACTER_DATA = {
    "cid": "00",
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

SAMPLE_ENEMY_DATA = [
    {
        "cid": "00",
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
        "cid": "00",
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
        "cid": "00",
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
        "cid": "00",
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

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.screen = Screen(width, height)

        # Game Assets
        self.hero = None
        self.players = []
        self.objects = []

        # Game State
        self.running = False
        self.input_text = ""

        # Load Data
        self.enemy_data = load_json("data/test_enemy_data.json")
        

    def __str__(self):
        s = f'w: {self.width}  h: {self.height}'
        return s

    def game_over(self, final_text: str="Winner Winner Chicken Dinner!"):
        os.system("cls")
        self.screen.reset_screen()
        
        # Redraw
        tblock = TextBlock(final_text)
        self.screen.add_string_block(final_text, (self.width - tblock.width//2 - 2)//2, (self.height - tblock.height - 2)//2)  # 51, 23
        print(self.screen)
        input()
    
#     main_char = Character(**CHARACTER_DATA)
    def battle(self, enemy):
       
        self.input_text = "[a]tk | [s]how | [q]uit"

        def enemy_turn():
            enemy_atks = ["hit"]
            idx = 0

            # Choose Random attack (if more than 1)
            if len(enemy_atks) > 1:
                idx = random.randint(0, len(enemy_atks) - 1)
            
            # Attack
            e_atk = enemy.get_attack(enemy_atks[idx])
            taken_damage = self.hero.take_hit(*e_atk)
            input(f"{enemy.name} used {enemy_atks[idx]}, {taken_damage} dmg done ")
            
            # Defend
            return

        def check_win():
            if not self.hero.is_alive:
                return True, enemy
            
            if not enemy.is_alive:
                return True, self.hero
            
            return False, None
        
        # Choose Turn order
        turns = ['hero', 'enemy']
        
        if enemy.speed > self.hero.speed:
            turns = ['enemy', 'hero']

        while True:
            # Clear display
            os.system("cls")

            # Reset Screen
            self.screen.reset_screen()

            # Draw on to screen
            char_txt = TextBlock(str(self.hero), border=True)
            enemy_txt = TextBlock(str(enemy), border=True)

            self.screen.add_string_block(f"{char_txt}", self.width - char_txt.width - 2, self.height - char_txt.height - 2)  # 51, 23
            self.screen.add_string_block(f"{enemy_txt}", 0, 0)  # 51, 23

            print(self.screen)

            for turn in turns:
                # Player Turn
                if turn == 'hero':
                    user_input = input(f"{self.input_text}>>> ")
                    # self.input_text = ""
                    match user_input:
                        case "q" | 'quit':
                            return
                        case 's' | "show":
                            atks = self.hero.show_attacks()
                            for a_name, a_data in atks.items():
                                print(f"{a_name}: {a_data[0]} dmg [{a_data[-1]}]")
                            input()
                        case "atk" | 'a':
                            # Display Attacks
                            atks = self.hero.show_attacks()
                            for a_name, a_data in atks.items():
                                print(f"{a_name}: {a_data[0]} dmg [{a_data[-1]}]")
                            
                            # Choose Attack
                            attack_name = input("Choose an attack: ")
                            
                            # Attack
                            my_atk = self.hero.get_attack(attack_name)
                            delt_damage = enemy.take_hit(*my_atk)
                            input(f"{self.hero.name} used {attack_name}, {delt_damage} dmg done ")
                        case _:
                            input(f"Invalid Input: {user_input}")

                if turn == 'enemy':
                    enemy_turn()
                    
                # Check WIn
                win, winner = check_win()

                if win:
                    self.input_text = ""
                    self.game_over(f'{winner.name} Wins!')
                    return

    def run(self):
        os.system("cls")
        
        # Start Game
        self.running = True

        # Create Hero
        print("What type of hero would you like to be?:")
        all_types = '\n'.join(h.name for h in (HeroTypes))
        hero_type = input(f"{all_types}\n>>> ")
        hero_name = input("Choose a name hero: ")
        
        hero_data = HeroTypes[hero_type.upper()].value

        self.hero = Character(cid="00", name=hero_name, level=1, **hero_data)
        input(f"Welcome {hero_name}, let's see what kind of {hero_type} you choose to be...")

        # Run Game
        while self.running:
            # Clear display
            os.system("cls")

            # Reset Screen
            self.screen.reset_screen()

            # Draw on to screen
            status_txt = TextBlock(self.hero.status_screen(), border=False)
            # enemy_txt = TextBlock(str(enemy), border=True)

            self.screen.add_string_block(f"{status_txt}", 0, 0)  # 51, 23
            # self.screen.add_string_block(f"{enemy_txt}", 0, 0)  # 51, 23

            # Draw screen on display
            print(self.screen)
            
            # Player and enemy Turns
            # Player Turn
            user_input = input(f"{self.input_text}>>> ")
            
            # Reset input text
            self.input_text = ""
            
            match user_input:
                case "q":
                    break
                case "battle":
                    enemy_idx = 0

                    # Show enemies
                    for _, e in enumerate(self.enemy_data):
                        print(_, e['name'])
                    
                    # Choose Enemy
                    enemy_idx = int(input('Choose Enemy #: '))

                    enemy = Character(**self.enemy_data[enemy_idx])
                    self.battle(enemy)
                case "stat":
                    input(self.hero.status_screen())
                case _:
                    # self.screen.add_string(user_input, 0, self.height - 1)
                    input(f"Invalid Input: {user_input}")

        return

if __name__ == "__main__":
#     CHARACTER_DATA = load_json("data/test_character_data.json")
#     ENEMY_DATA = load_json("data/test_enemy_data.json")

#     width, height = os.get_terminal_size()
#     self.width, SCREEN_HEIGHT = width - 2, height -3
#     SCREEN = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

#     # if load data doesnt exist

#     # character_data = save_json(SAMPLE_CHARACTER_DATA, "data/test_character_data.json")
#     # enemies_data = save_json(SAMPLE_ENEMY_DATA, "data/test_enemy_data.json")

#     main_char = Character(**CHARACTER_DATA)
#     enemy = Character(**ENEMY_DATA[0])

#     char_txt = TextBlock(str(main_char), border=True)
#     enemy_txt = TextBlock(str(enemy), border=True)

#     # print(SCREEN_WIDTH - char_txt.width - 2, SCREEN_HEIGHT - char_txt.height - 2)
#     # print(f"{char_txt}")
#     # input()

#     SCREEN.add_string_block(f"{char_txt}", SCREEN_WIDTH - char_txt.width - 2, SCREEN_HEIGHT - char_txt.height - 2)  # 51, 23
#     SCREEN.add_string_block(f"{enemy_txt}", 0, 0)  # 51, 23

#     UPDATE_TEXT = ""


#     def enemy_turn():
#         # Attack
#         enemy_atk_name = "hit"
#         e_atk = enemy.get_attack(enemy_atk_name)
#         taken_damage = main_char.take_hit(*e_atk)
#         print(f"{enemy.name} used {enemy_atk_name}, {taken_damage} dmg done ")
#         input()
        
#         # Defend
#         return
    

#     def check_win():
#         if not main_char.is_alive or not enemy.is_alive:            
#             winner = main_char if main_char.is_alive else enemy
#             return True, winner
#         return False, None
    
#     def game_over(winner_name):
#         os.system("cls")
#         SCREEN.reset_screen()
        
#         # Redraw
#         SCREEN.add_string_block(f"{winner_name} Wins!", (SCREEN_WIDTH - char_txt.width//2 - 2)//2, (SCREEN_HEIGHT - char_txt.height//2 - 2)//2)  # 51, 23
#         print(SCREEN)

    

#     while True:
#         os.system("cls")
#         char_txt = TextBlock(str(main_char), border=True)
#         enemy_txt = TextBlock(str(enemy), border=True)

#         SCREEN.add_string_block(f"{char_txt}", SCREEN_WIDTH - char_txt.width - 2, SCREEN_HEIGHT - char_txt.height - 2)  # 51, 23
#         SCREEN.add_string_block(f"{enemy_txt}", 0, 0)  # 51, 23

#         print(SCREEN)

#         enemy_turn_played = False
#         if enemy.speed > main_char.speed:
#             enemy_turn()
#             enemy_turn_played = True
#             # Check WIn
#             win, winner = check_win()

#             if win:
#                 game_over(winner.name)
#                 break

#         # Player Turn
#         user_input = input(f"{UPDATE_TEXT}>>> ")
#         UPDATE_TEXT = ""
#         match user_input:
#             case "q":
#                 break
#             case "d":
#                 atks = main_char.show_attacks()
#                 for a_name, a_data in atks.items():
#                     print(f"{a_name}: {a_data[0]} dmg [{a_data[-1]}]")
#                 input()
#             case "a":
#                 attack_name = "hit"
#                 my_atk = main_char.get_attack(attack_name)
#                 taken_damage = enemy.take_hit(*my_atk)
#                 UPDATE_TEXT = f"{main_char.name} used {attack_name}, {taken_damage} dmg done "
#             case _:
#                 SCREEN.add_string(user_input, 0, SCREEN_HEIGHT - 1)
#                 # input("Invalid Input")
        
#         # Check WIn
#         win, winner = check_win()

#         if win:
#             game_over(winner.name)
#             break

#         if not enemy_turn_played:
#             enemy_turn()

#             # Check WIn
#             win, winner = check_win()

#             if win:
#                 game_over(winner.name)
#                 break


# for htype in (HeroTypes):
#     print(f"{htype.name}")    
    width, height = os.get_terminal_size()
    SCREEN_WIDTH, SCREEN_HEIGHT = width - 2, height -3

    new_game = Game(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    new_game.run()


