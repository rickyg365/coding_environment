
from dataclasses import dataclass
from utils.status_bar import status_bar

'''
* Goal: each Character keeps track of their own state
Character
    name: str
    hp: int
    mp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int
    luck: int

    current_hp: int
    currnet_mp: int

    is_alive: bool

'''
# class Character:
#     def __init__(self, name: str=None, level: int=0, hp: int=None, mp: int=None, attack: int=None, defense: int=None, special_attack: int=None, special_defense: int=None, speed: int=None, luck: int=None):
#         # Attributes
#         self.level = level
#         self.name = name
        
#         self.hp = hp
#         self.mp = mp
        
#         self.attack = attack
#         self.defense = defense
#         self.special_attack = special_attack
#         self.special_defense = special_defense
#         self.speed = speed
#         self.luck = luck

#         # Status
#         self.is_alive = True

#         self.current_hp = hp
#         self.currnet_mp = mp

#         self.experience = 0
#         self.accumulated_experience = []

@dataclass
class Character:
    name: str
    level: int
    hp: int = 10 
    mp: int = 0 
    attack: int = 0 
    defense: int = 0 
    special_attack: int = 0 
    special_defense: int = 0 
    speed: int = 0 
    luck: int = 0 
    is_alive: bool = True
    experience: int = 0

    # Meta
    textbox_width: int = 0
    textbox_height: int = 0

    def __post_init__(self):
        self.current_hp = self.hp 
        self.currnet_mp = self.mp

    def __str__(self):
        custom_config = {
            "l": "[",
            "r": "]",
            "fill": "=",
            "space": " ",
        }
        
        row1 = f'lvl.{self.level:2}  {self.name}'
        row2 = f"HP {status_bar(self.current_hp, self.hp, config=custom_config)}"
        s = f'{row1:<{len(row2)}}\n{row2}'
        return s
    
    def add_experience(self, value: int, types):
        exp_conj = 100 - self.experience
        if value > exp_conj:
            self.experience = value - exp_conj
            # Add accum exp
        else:
            self.experience += value
            # Add accum exp
            self.accumulated_experience += types

    
    def export(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "mp": self.mp,
            "attack": self.attack,
            "defense": self.defense,
            "special_attack": self.special_attack,
            "special_defense": self.special_defense,
            "speed": self.speed,
            "luck": self.luck,
            "is_alive": self.is_alive,
            "current_hp": self.current_hp,
            "currnet_mp": self.currnet_mp,
            "experience": self.experience,
            # "accumulated_experience": self.accumulated_experience,
        }

