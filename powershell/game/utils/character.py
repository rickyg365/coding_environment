from typing import Self, List, Dict
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
    cid: str 
    name: str
    level: int
    max_health: int = 10 
    current_health: int = 0 
    max_mp: int = 0 
    current_mp: int = 0

    attack: int = 0 
    defense: int = 0 
    special_attack: int = 0 
    special_defense: int = 0 
    speed: int = 0 
    luck: int = 0 
    is_alive: bool = True
    experience: int = 0
    attacks: Dict = None

    # Meta
    textbox_width: int = 0
    textbox_height: int = 0

    def __post_init__(self):
        self.current_health = self.max_health if self.current_health == 0 else self.current_health 
        self.current_mp = self.max_mp if self.current_mp == 0 else self.current_mp

        if self.attacks is None:
            # self.attacks = dict()
            self.attacks = {
                "hit": (10, self.attack, None)
            }

    def __str__(self):
        custom_config = {
            "l": "[",   
            "r": "]",
            "fill": "=",
            "space": " ",
        }
        
        row1 = f'lvl.{self.level:2}  {self.name}'
        row2 = f"HP {status_bar(self.current_health, self.max_health, config=custom_config)}"
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
    
    def take_hit(self, damage_amount, enemy_atk, status_conditions):
        ad_dif = enemy_atk - self.defense
        full_damage_amt = damage_amount + ad_dif
        self.current_health -= full_damage_amt

        # Check status
        if self.current_health <= 0:
            self.is_alive = False
            self.current_health = 0
        
        # Handle status conditions
        if status_conditions is not None:
            pass
        
        return full_damage_amt
    
    def get_attack(self, atk_name: str="hit"):
        return self.attacks.get(atk_name, (0, self.attack, None))
    
    def show_attacks(self):
        # "hit": (10, self.attack, None)
        for atk_name, atk_data in self.attacks.items():
            ...
        return self.attacks
    
    def export(self):
        return {
            "cid": self.cid,
            "name": self.name,
            "hp": self.max_health,
            "mp": self.max_mp,
            "attack": self.attack,
            "defense": self.defense,
            "special_attack": self.special_attack,
            "special_defense": self.special_defense,
            "speed": self.speed,
            "luck": self.luck,
            "is_alive": self.is_alive,
            "current_hp": self.current_health,
            "currnet_mp": self.currnet_mp,
            "experience": self.experience,
            # "accumulated_experience": self.accumulated_experience,
        }

