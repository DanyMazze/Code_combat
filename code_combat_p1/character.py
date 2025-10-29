from weapon import Weapon
from potion import Potion

class Character:
    def __init__(self, name: str, max_hp: int, strength: int, dextrety: int, weapon = None, potions = None):
        self.__name = name
        self.__max_hp = max_hp
        self.__hp = self.__max_hp
        self.__strength = strength
        self.__dextrety = dextrety
        self.__weapon = weapon
        self.__potions = potions
        self.__buffs = []


    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name: str):
        if new_name == "":
            new_name = "unamed"
        self.__name = new_name

    @property
    def max_hp(self):
        return self.__max_hp
    
    @property
    def hp(self):
        return self.__hp
    
    @property
    def strength(self):
        return self.__strength
    
    @property
    def dextrety(self):
        return self.__dextrety
    
    @property
    def weapon(self):
        return self.__weapon
    
    @weapon.setter
    def weapon(self, new_weapon: Weapon):
        if not isinstance(new_weapon, Weapon):
            new_weapon = None  
        self.__weapon = new_weapon

    def __modifier(self, attribute: int) -> int:
        return (attribute - 10) // 2
    
    def is_alive(self) -> bool:
        if self.__hp <= 0:
            return False
        return True
    
    def __take_damage(self, damage: int) -> int:
        if damage > self.__hp:
            damage = self.__hp
        self.__hp = self.__hp - damage
        return damage
    
    def attack(self, enemy: 'Character') -> int:
        if self.__weapon is None:
            damage = 1
        if self.__weapon.type == "melee":
            damage = (self.__weapon.get_damage() + self.__modifier(self.__strength))
        else:
            damage = (self.__weapon.get_damage() + self.__modifier(self.__dextrety))
        if damage < 0:
            damage = 0
        damage_effective = enemy.__take_damage(damage)
        return damage_effective
    
    def __heal(self, value: int) -> int:
        if value > self.__max_hp:
            value = self.__max_hp
        self.__hp += value
        return value

    def __add_buff(self, attribute: str, amount: int) -> int:
        actual_amount = amount
        if attribute == "strength":
            if self.__strength + amount > 20:
                actual_amount = 20 - self.__strength
            self.__strength += actual_amount
            self.__buffs.append(("strength", actual_amount)) 
        elif attribute == "dextrety": 
            if self.__dextrety + amount > 20:
                actual_amount = 20 - self.__dextrety
            self.__dextrety += actual_amount
            self.__buffs.append(("dextrety", actual_amount))  
        return actual_amount

    def tick_buff(self):
        for buff_type, amount in self.__buffs:
            if buff_type == "strength":
                self.__strength -= amount
            elif buff_type == "dextrety":
                self.__dextrety -= amount
        self.__buffs = []  
    
    def __should_use_potion_healt(self) -> bool:
        if self.__hp / self.__max_hp < 0.333:
            return True
        return False
    
    def __should_use_potion_buff(self) -> bool:
        if len(self.__buffs) == 0:
            return True
        return False
    
    def should_use_potion(self) -> str:
        if self.__should_use_potion_healt():
            return "health"
        if self.__should_use_potion_buff():
            return "buff"
        return "none"
    
    def have_potion(self, potion: Potion) -> bool:
        if potion in self.__potions:
            return True
        return False
    
    def use_potion(self, potion: Potion):
        value = 0
        if potion.effect == "health":
            value = self.__heal(potion.amount)
            self.__potions.remove(potion)
        elif potion.effect == "buff": 
            self.__add_buff(potion.attribute, potion.amount)
            self.__potions.remove(potion)
            value = potion.duration
        return value

    def __str__(self):
        return f"{self.__name}: {self.__hp}/{self.__max_hp} - str:{self.__strength}, dex:{self.__dextrety} - status: {self.__buffs} - potions: {self.__potions}"


