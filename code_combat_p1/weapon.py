from random import randint
class Weapon:
    def __init__(self, name: str, type: str, min_damage: int, max_damage: int):
        if name == "":
            raise ValueError("name cannot be empty")
        if type not in ["melee", "ranged"]:
            raise ValueError("type must be 'melee' or 'ranged'")
        if min_damage < 1:
            raise ValueError("min_damage must be >= 1")
        if max_damage < min_damage:
            raise ValueError("max_damage must be >= min_damage")
        self.__name = name
        self.__type = type
        self.__min_damage = min_damage
        self.__max_damage = max_damage

    @property
    def name(self):
        return self.__name
    
    @property
    def type(self):
        return self.__type
    
    @property
    def min_damage(self):
        return self.__min_damage
    
    @property
    def max_damage(self):
        return self.__max_damage
    
    def get_damage(self):
        return randint(self.__min_damage, self.__max_damage)
    
    def __str__(self):
        return f"{self.__name}: {self.__min_damage}/{self.__max_damage} - {self.__type}"
