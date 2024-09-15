import os
import json

from utils.text_block import TextBlock
from utils.screen import Screen
from utils.character import Character


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



if __name__ == "__main__":
    CHARACTER_DATA = load_json("data/test_character_data.json")
    ENEMY_DATA = load_json("data/test_enemy_data.json")

    width, height = os.get_terminal_size()
    SCREEN_WIDTH, SCREEN_HEIGHT = width - 2, height -3
    SCREEN = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

    # if load data doesnt exist

    # character_data = save_json(SAMPLE_CHARACTER_DATA, "data/test_character_data.json")
    # enemies_data = save_json(SAMPLE_ENEMY_DATA, "data/test_enemy_data.json")

    main_char = Character(**CHARACTER_DATA)
    enemy = Character(**ENEMY_DATA[0])

    char_txt = TextBlock(str(main_char), border=True)
    enemy_txt = TextBlock(str(enemy), border=True)

    # print(SCREEN_WIDTH - char_txt.width - 2, SCREEN_HEIGHT - char_txt.height - 2)
    # print(f"{char_txt}")
    # input()

    SCREEN.add_string_block(f"{char_txt}", SCREEN_WIDTH - char_txt.width - 2, SCREEN_HEIGHT - char_txt.height - 2)  # 51, 23
    SCREEN.add_string_block(f"{enemy_txt}", 0, 0)  # 51, 23

    UPDATE_TEXT = ""


    def enemy_turn():
        # Attack
        enemy_atk_name = "hit"
        e_atk = enemy.get_attack(enemy_atk_name)
        taken_damage = main_char.take_hit(*e_atk)
        print(f"{enemy.name} used {enemy_atk_name}, {taken_damage} dmg done ")
        input()
        
        # Defend
        return
    

    def check_win():
        if not main_char.is_alive or not enemy.is_alive:            
            winner = main_char if main_char.is_alive else enemy
            return True, winner
        return False, None
    
    def game_over(winner_name):
        os.system("cls")
        SCREEN.reset_screen()
        
        # Redraw
        SCREEN.add_string_block(f"{winner_name} Wins!", (SCREEN_WIDTH - char_txt.width//2 - 2)//2, (SCREEN_HEIGHT - char_txt.height//2 - 2)//2)  # 51, 23
        print(SCREEN)

    

    while True:
        os.system("cls")
        char_txt = TextBlock(str(main_char), border=True)
        enemy_txt = TextBlock(str(enemy), border=True)

        SCREEN.add_string_block(f"{char_txt}", SCREEN_WIDTH - char_txt.width - 2, SCREEN_HEIGHT - char_txt.height - 2)  # 51, 23
        SCREEN.add_string_block(f"{enemy_txt}", 0, 0)  # 51, 23

        print(SCREEN)

        enemy_turn_played = False
        if enemy.speed > main_char.speed:
            enemy_turn()
            enemy_turn_played = True
            # Check WIn
            win, winner = check_win()

            if win:
                game_over(winner.name)
                break

        # Player Turn
        user_input = input(f"{UPDATE_TEXT}>>> ")
        UPDATE_TEXT = ""
        match user_input:
            case "q":
                break
            case "d":
                atks = main_char.show_attacks()
                for a_name, a_data in atks.items():
                    print(f"{a_name}: {a_data[0]} dmg [{a_data[-1]}]")
                input()
            case "a":
                attack_name = "hit"
                my_atk = main_char.get_attack(attack_name)
                taken_damage = enemy.take_hit(*my_atk)
                UPDATE_TEXT = f"{main_char.name} used {attack_name}, {taken_damage} dmg done "
            case _:
                SCREEN.add_string(user_input, 0, SCREEN_HEIGHT - 1)
                # input("Invalid Input")
        
        # Check WIn
        win, winner = check_win()

        if win:
            game_over(winner.name)
            break

        if not enemy_turn_played:
            enemy_turn()

            # Check WIn
            win, winner = check_win()

            if win:
                game_over(winner.name)
                break

        
