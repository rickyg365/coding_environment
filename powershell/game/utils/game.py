import os
import random

from utils.file_handle import load_json, save_json
from utils.text_block import TextBlock
from utils.screen import Screen
from utils.character import Character, HeroTypes


class Game:
    MAIN_LOAD_PATH = r'C:\Users\ricky\Documents\PowerShell\game\data\main_save.json'
    ENEMY_DATA_PATH = r'C:\Users\ricky\Documents\PowerShell\game\data\enemy_data.json'

    def __init__(self, width, height, load_path: str=None):
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
        self.enemy_data = load_json(self.ENEMY_DATA_PATH)
        self.load_path = load_path

        # Load game data
        if load_path is None:
            self.load_path = self.MAIN_LOAD_PATH
        
    def __str__(self):
        s = f'w: {self.width}  h: {self.height}'
        return s
    
    def load_game(self, path: str=MAIN_LOAD_PATH):
        data = load_json(path)
        hero_data = data.get('hero', None)
        self.hero = Character(**hero_data)
    
    def save_game(self, path: str=MAIN_LOAD_PATH):
        export_data = {
            'hero': self.hero.export()
        }
        save_json(export_data, path)
        # return export_data

    def game_over(self, final_text: str="Winner Winner Chicken Dinner!"):
        # Clear Display and Screen
        os.system("cls")
        self.screen.reset_screen()
        
        # Delete Save Data
        if os.path.exists(self.load_path):
            os.remove(self.load_path)


        # Draw final text on screen center
        tblock = TextBlock(final_text)  # Text info
        cx = (self.width - tblock.width//2 - 6)//2
        cy = (self.height - tblock.height - 2)//2
        
        self.screen.add_string_block(final_text, cx, cy)  # 51, 23
        print(self.screen)
        
        # Let user see at own pace
        input()


    def create_new_hero(self):
        # Get Hero Data
        hero_name = input("Choose a name hero: ")

        print("What type of hero would you like to be?:")
        all_types = '\n'.join(h.name for h in (HeroTypes))
        hero_type = input(f"{all_types}\n>>> ")
        
        hero_data = HeroTypes[hero_type.upper()].value

        # Create Hero
        self.hero = Character(cid="00", name=hero_name, level=1, **hero_data)
        input(f"\nWelcome {hero_name}, let's see what kind of {hero_type} you choose to be...")

#     main_char = Character(**CHARACTER_DATA)
    def battle(self, enemy): 
        self.input_text = "[a]tk | [s]how "
        # self.input_text = "[a]tk | [s]how | [q]uit "

        def enemy_turn():
            enemy_atks = ["hit"]
            idx = 0

            # Choose Random attack (if more than 1)
            if len(enemy_atks) > 1:
                idx = random.randint(0, len(enemy_atks) - 1)
            
            # Attack
            taken_damage = enemy.use_attack(enemy_atks[idx], self.hero)
            input(f"{enemy.name} used {enemy_atks[idx]}, {taken_damage} dmg done ")
            
            # Defend
            return
        
        def player_turn():
            user_input = input(f"{self.input_text}>>> ")
            # self.input_text = ""
            match user_input:
                case 's' | "show":
                    print()
                    atks = self.hero.show_attacks()
                    for a_name, a_data in atks.items():
                        print(f"{a_name}: {a_data[0]} dmg [{a_data[-1]}]")
                    input()
                case "atk" | 'a':
                    # Display Attacks
                    print()
                    atks = self.hero.show_attacks()
                    for a_name, a_data in atks.items():
                        print(f"{a_name}: {a_data[0]} dmg [{a_data[-1]}]")
                    
                    # Choose Attack
                    attack_name = input("\nChoose an attack: ")
                    
                    # Attack
                    self.hero.get_attack()
                    delt_damage = self.hero.use_attack(attack_name, enemy)
                    input(f"{self.hero.name} used {attack_name}, {delt_damage} dmg done ")
                case _:
                    input(f"Invalid Input: {user_input}")


        # Choose Turn order
        turns = ['hero', 'enemy']
        
        if enemy.speed > self.hero.speed:
            turns = ['enemy', 'hero']

        # Main Battle loop
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
                    player_turn()
                if turn == 'enemy':
                    enemy_turn()
                    
                # Check WIn
                win = False
                winner = enemy.name
                if not self.hero.is_alive or not enemy.is_alive:
                    win = True

                if win:
                    if self.hero.is_alive:
                        winner = self.hero.name
                        # enemy.experience_reward
                        self.hero.add_experience(70)
                    self.input_text = ""
                    self.game_over(f'{winner} Wins!')
                    return self.hero.is_alive

    def run(self):
        os.system("cls")
        
        # Start Game
        self.running = True
        self.input_text = "[b]attle | [c]reate new hero | [s]ave | [q]uit "

        # Check if load data exist
        if not os.path.exists(self.load_path):
           self.create_new_hero()
        else:
            self.load_game(self.load_path)

        # Run Game
        while self.running:
            # Clear display
            os.system("cls")

            # Reset Screen
            self.screen.reset_screen()

            # Draw on to screen
            status_txt = TextBlock(self.hero.status_screen(), border=False)

            self.screen.add_string_block(f"{status_txt}", 0, 0)  # 51, 23

            # Draw screen on display
            print(self.screen)
            
            # Turns
            # Player Turn
            user_input = input(f"{self.input_text}>>> ")
            
            # Reset input text
            self.input_text = ""
            
            match user_input:
                case "q":
                    # if self.hero.is_alive:
                    #     self.save_game(self.load_path)
                    break
                case "c":
                    self.create_new_hero()
                case "s":
                    if self.hero.is_alive:
                        self.save_game(self.load_path)
                    else:
                        print("Can't save after you've been defeated!")
                case 'b' | "battle":
                    enemy_idx = 0

                    # Show enemies
                    # for _, e in enumerate(self.enemy_data):
                    #     print(_, e['name'])
                    
                    # Choose Enemy
                    # enemy_idx = int(input('Choose Enemy #: '))
                    
                    # Choose Random Enemy
                    enemy_idx = random.randint(0, len(self.enemy_data) - 1)
                    # Inform player of their fate
                    input(f"Prepare to battle... {self.enemy_data[enemy_idx].get('name', '???')}")

                    enemy = Character(**self.enemy_data[enemy_idx])
                    player_win = self.battle(enemy)
                    if not player_win:
                        break
                # case "stat":
                #     input(self.hero.status_screen())
                case _:
                    # self.screen.add_string(user_input, 0, self.height - 1)
                    input(f"Invalid Input: {user_input}")

        return
