from typing import Self, List, Dict
from enum import Enum
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
    current_mp: int

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
#         self.current_mp = mp

#         self.experience = 0
#         self.accumulated_experience = []




'''
st1:st2  Basic Hero > Evolution
def:sdf  knight > Paladin
def:stk  knight > Magic Knight
def:spd  knight > Gaurd
def:atk  knight > Champion
def:def  knight > Tank

stk:sdf  mage > Wizard
stk:spd  mage > Trickster/Magician
stk:atk  mage > Enchanter
stk:def  mage > Cleric
stk:stk  mage > Sage

atk:sdf  fighter > Monk
atk:stk  fighter > Battle Mage
atk:spd  fighter > Assasain
atk:def  fighter > Warrior
atk:atk  fighter > Beserker

atk:sdf  archer > Trapper
atk:stk  archer > Mystic Archer
atk:spd  archer > Sharpshooter
atk:def  archer > Ranger
atk:atk  archer > Canoneer

'''


# Starter Types
class HeroTypes(Enum):
    KNIGHT = {
        "max_hp": 30,
        "max_mp": 5,
        "attack": 6,
        "defense": 9,
        "special_attack": 5,
        "special_defense": 6,
        "speed": 4,
        "luck": 1,
        "hp_growth": 12,
        "mp_growth": 3,
        "atk_growth": 4,
        "def_growth": 6,
        "satk_growth": 3,
        "sdef_growth": 5,
        "spd_growth": 4,
    }

    MAGE = {
        "max_hp": 20,
        "max_mp": 10,
        "attack": 4,
        "defense": 3,
        "special_attack": 10,
        "special_defense": 6,
        "speed": 7,
        "luck": 1,
        "hp_growth": 5,
        "mp_growth": 10,
        "atk_growth": 3,
        "def_growth": 3,
        "satk_growth": 6,
        "sdef_growth": 5,
        "spd_growth": 5,
    }

    FIGHTER = {
        "max_hp": 25,
        "max_mp": 5,
        "attack": 8,
        "defense": 5,
        "special_attack": 7,
        "special_defense": 3,
        "speed": 7,
        "luck": 1,
        "hp_growth": 10,
        "mp_growth": 5,
        "atk_growth": 6,
        "def_growth": 4,
        "satk_growth": 4,
        "sdef_growth": 3,
        "spd_growth": 5,
    }

    ARCHER = {
        "max_hp": 20,
        "max_mp": 8,
        "attack": 9,
        "defense": 3,
        "special_attack": 6,
        "special_defense": 4,
        "speed": 8,
        "luck": 2,
        "hp_growth": 5,
        "mp_growth": 7,
        "atk_growth": 6,
        "def_growth": 3,
        "satk_growth": 5,
        "sdef_growth": 3,
        "spd_growth": 5,
    }



@dataclass
class Character:
    cid: str 
    name: str
    level: int = 0
    max_hp: int = 10 
    current_hp: int = 0 
    max_mp: int = 0 
    current_mp: int = 0

    attack: int = 0 
    defense: int = 0 
    special_attack: int = 0 
    special_defense: int = 0 
    speed: int = 0 
    luck: int = 0 
    
    attacks: Dict = None
    # Growth
    experience: int = 0
    hp_growth:int = 10
    mp_growth: int = 5
    atk_growth: int = 5
    def_growth: int = 5
    satk_growth: int = 5
    sdef_growth: int = 5
    spd_growth: int = 5

    # Meta
    is_alive: bool = True
    textbox_width: int = 0
    textbox_height: int = 0

    def __post_init__(self):
        self.current_hp = self.max_hp if self.current_hp == 0 else self.current_hp 
        self.current_mp = self.max_mp if self.current_mp == 0 else self.current_mp

        if self.attacks is None:
            # self.attacks = dict()
            self.attacks = {
                "hit": (25, "none", None),
                "slash": (15, "attack", None),
                "magic shot": (15, "special_attack", None),
                "shield blow": (15, "defense", None),
                "inner power": (100, "all", None),
            }

    def __str__(self):
        custom_config = {
            "l": "[",   
            "r": "]",
            "fill": "=",
            "space": " ",
        }
        
        row1 = f'lvl.{self.level:2}  {self.name}'
        row2 = f"HP {status_bar(self.current_hp, self.max_hp, config=custom_config)}"
        s = f'{row1:<{len(row2)}}\n{row2}'
        return s
    
    def level_up(self):
        self.level += 1

        # Update Stats
        self.max_hp += self.hp_growth
        self.current_hp = self.max_hp
        self.max_mp += self.mp_growth
        self.current_mp = self.max_mp
        self.attack += self.atk_growth
        self.defense += self.def_growth
        self.speed += self.spd_growth
        self.special_attack += self.satk_growth
        self.special_defense += self.sdef_growth
        self.luck += 1

    
    def add_experience(self, value: int):
        exp_conj = 100 - self.experience
        if value >= exp_conj:
            self.level_up()
            self.experience = 0

            self.add_experience(value - exp_conj)
            # Add accum exp
            return
        
        self.experience += value
        # Add accum exp
        # self.accumulated_experience += types

    def take_hit(self, damage_amount):
        self.current_hp -= damage_amount

        # Check status
        if self.current_hp <= 0:
            self.is_alive = False
            self.current_hp = 0
        
        return damage_amount
    
    def get_attack(self, atk_name: str="hit"):
        return self.attacks.get(atk_name, (0, self.attack, None))
    
    def use_attack(self, chosen_atk: str, enemy):
        atk = self.get_attack(chosen_atk)
        dmg, modifier, status_condition = atk

        m = 0
        match modifier:
            case "attack":
                m = self.attack
            case "defense":
                m = self.defense
            case "special_defense":
                m = self.special_defense
            case "special_attack":
                m = self.special_attack
            case "speed":
                m = self.speed
            case "all":
                m = self.attack + self.defense + self.special_attack + self.special_defense + self.speed
            case _:
                m = 0

        full_damage_amount = abs(dmg + m - enemy.defense)

        # Update Enemy Status
        enemy.take_hit(full_damage_amount)

        # Status conditions
        return full_damage_amount
    
    def show_attacks(self):
        # "hit": (10, self.attack, None)
        for atk_name, atk_data in self.attacks.items():
            ...
        return self.attacks
    
    def status_screen(self):
        custom_config = {
            "l": "[",   
            "r": "]",
            "fill": "=",
            "space": " ",
        }
        
        exp_config = {
            "l": "[",   
            "r": "]",
            "fill": "@",
            "space": " ",
        }
        
        return f"""lvl.{self.level:2}  {self.name}
HP {self.current_hp:>3}/{self.max_hp:<3} {status_bar(self.current_hp, self.max_hp, config=custom_config)}
MP {self.current_mp:>3}/{self.max_mp:<3} {status_bar(self.current_mp, self.max_mp, config=custom_config)}

Attack: {self.attack}
Defense: {self.defense}
Special Attack: {self.special_attack}
Special Defense: {self.special_defense}
Speed: {self.speed}
Luck: {self.luck}

EXP: {status_bar(self.experience, 100, config=exp_config)}

"""
    
    def export(self):
        return {
            "cid": self.cid,
            "level": self.level,
            "name": self.name,
            "max_hp": self.max_hp,
            "max_mp": self.max_mp,
            "attack": self.attack,
            "defense": self.defense,
            "special_attack": self.special_attack,
            "special_defense": self.special_defense,
            "speed": self.speed,
            "luck": self.luck,
            "is_alive": self.is_alive,
            "current_hp": self.current_hp,
            "current_mp": self.current_mp,
            "experience": self.experience,
            "hp_growth": self.hp_growth,
            "mp_growth": self.mp_growth,
            "atk_growth": self.atk_growth,
            "def_growth": self.def_growth,
            "satk_growth": self.satk_growth,
            "sdef_growth": self.sdef_growth,
            "spd_growth": self.spd_growth,
        }
    

