import os

def status_bar(current, max, bar_width: int=20, config=None):
    default_config = {
        "fill": "█",
        "space": " ",
        "l_end": "│",
        "r_end": "│" 
    }
    if config is None:
        config = {**default_config}

    ratio = current/max
    fill = int(bar_width * ratio)

    # overides
    if current > 0 and fill == 0:
        fill = 1
    
    space = bar_width - fill
    
    l_end = config.get('l_end', default_config['l_end'])
    r_end = config.get('r_end', default_config['r_end'])
    fill_char = config.get('fill', default_config['fill'])
    space_char = config.get('space', default_config['space'])

    return f"{l_end}{fill * fill_char}{space * space_char}{r_end}"


class Character:
    ID_DEFAULT = 0
    NAME_DEFAULT = "No Name"
    
    LEVEL_DEFAULT = 0

    HP_DEFAULT = 20
    MP_DEFAULT = 10
    
    ATTACK_DEFAULT = 0
    DEFENSE_DEFAULT = 0
    SPECIAL_ATTACK_DEFAULT = 0
    SPECIAL_DEFENSE_DEFAULT = 0
    SPEED_DEFAULT = 0
    LUCK_DEFAULT = 0

    def __init__(self, **character_data):
        self.id = character_data.get('id', self.ID_DEFAULT)
        self.name = character_data.get('name', self.NAME_DEFAULT)

        # Stats
        self.level = character_data.get('level', self.LEVEL_DEFAULT)

        self.current_health = character_data.get('current_hp', self.HP_DEFAULT)
        self.max_health = character_data.get('max_hp', self.HP_DEFAULT)

        self.current_mp = character_data.get('current_mp', self.MP_DEFAULT)
        self.max_mp = character_data.get('max_mp', self.MP_DEFAULT)


        self.attack = character_data.get('attack', self.ATTACK_DEFAULT)
        self.defense = character_data.get('defense', self.DEFENSE_DEFAULT)
        self.special_attack = character_data.get('special_attack', self.SPECIAL_ATTACK_DEFAULT)
        self.special_defense = character_data.get('special_defense', self.SPECIAL_DEFENSE_DEFAULT)
        self.speed = character_data.get('speed', self.SPEED_DEFAULT)
        self.luck = character_data.get('luck', self.LUCK_DEFAULT)

    def __str__(self):


        top_status = f"lvl.{self.level:>2}  {self.name}"
        hp_status = f"HP: {self.current_health:<3}/{self.max_health:<3} {status_bar(self.current_health, self.max_health)}"
        mp_status = f"MP: {self.current_mp:<3}/{self.max_mp:<3} {status_bar(self.current_mp, self.max_mp, bar_width=self.max_mp if self.max_mp < 21 else 20)}"

        s = f'''{top_status}
{hp_status}
{mp_status}'''
        return s
    

class Hero:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        s = f'{self.name}'
        return s
    

class Enemy:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        s = f'{self.name}'
        return s
    


if __name__ == "__main__":
    SAMPLE_CHARACTER_DATA = {
        "id": "01",
        "name": "Hero",
        "level": 1,
        "current_health": 30,
        "max_health": 30,
        "current_mp": 10,
        "max_mp": 10,
        "attack": 7,
        "defense": 5,
        "special_attack": 5,
        "special_defense": 5,
        "speed": 6,
        "luck": 2,
    }
    new_hero = Character(**SAMPLE_CHARACTER_DATA)
    print(new_hero)
