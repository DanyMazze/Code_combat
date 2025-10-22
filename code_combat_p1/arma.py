from random import randint

class Weapon:
    def __init__(self, min_damage: int, max_damage: int, name: str, type: str):
        if min_damage < 0:
            min_damage = 0
        if min_damage > max_damage:
            max_damage = min_damage + 1
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__name = name
        if type == "melee" or type == "ranged":
            type = type
        else:
            type = "melee"
        self.__type = type
        
    @property
    def min_damage(self):
        return self.__min_damage
    
    @min_damage.setter
    def min_damage(self, value: int):
        if value < 0:
            value = 0
        if value > self.max_damage:
            value = self.max_damage
        self.__min_damage = value
        
    @property
    def max_damage(self):
        return self.__max_damage
    
    @max_damage.setter
    def max_damage(self, value: int):
        if value < self.min_damage:
            value = self.min_damage + 1
        self.__max_damage = value
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if not value:
            value = "Unknown"
        self.__name = value
        
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, value: str):
        if value not in ["melee", "ranged"]:
            value = "melee"
        self.__type = value

    def get_damage(self):
        return randint(self.__min_damage, self.__max_damage)

    def __str__(self):
        return f"{self.__name} ({self.__type}): {self.__min_damage}-{self.__max_damage} damage"
