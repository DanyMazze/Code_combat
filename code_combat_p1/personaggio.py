from arma import Weapon

class Character:
    def __init__(self, name: str, max_hp: int, strength: int, dexterity: int, weapon = None, potions = None):
        self.__name = name
        if max_hp < 1:
            max_hp = 1
        self.max_hp = max_hp
        self.__hp = max_hp
        if strength < 0:
            strength = 0
        self.__strength = strength
        if dexterity < 0:
            dexterity = 0
        self.__dexterity = dexterity
        self.__weapon = weapon
        self.__buff =  None

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value: str):
        if not value:
            value = "Unknown"
        self.__name = value

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value: int):
        if value < 0:
            value = 0
        elif value > self.max_hp:
            value = self.max_hp
        self.__hp = value

    @property
    def strength(self):
        return self.__strength
    @strength.setter
    def strength(self, value: int):
        if value < 0:
            value = 0
        self.__strength = value

    @property
    def dexterity(self):
        return self.__dexterity
    @dexterity.setter
    def dexterity(self, value: int):
        if value < 0:
            value = 0
        self.__dexterity = value

    @property
    def weapon(self):
        return self.__weapon
    @weapon.setter
    def weapon(self, value: Weapon):
        if not isinstance(value, Weapon):
            value = None
        self.__weapon = value

    def modifier(self, value: int) -> int:
        return (value - 10) // 2
    
    def is_alive(self) -> bool:
        return self.hp > 0
    
    def __take_damage(self, damage: int) -> int:
        if damage >= self.hp:
            damage = self.hp
        self.hp -= damage
        return damage
    
    def heal(self, amount: int):
        if amount < 0:
            amount = 0
        if self.hp + amount > self.max_hp:
            amount = self.max_hp - self.hp
        self.hp += amount

    def __add_buff(self, attribute: str, amount: int):
        if attribute == "strength":
            if amount < 0 or self.strength + amount > 20:
                return
            self.strength += amount
        elif attribute == "dexterity":
            if amount < 0 or self.dexterity + amount > 20:
                return
            self.dexterity += amount

    def attack(self, target: "Character"):
        if self.weapon is None:
            damage = 1
        else:
            if self.weapon.type == "melee":
                damage = self.weapon.get_damage() + self.modifier(self.strength)
            elif self.weapon.type == "ranged":
                damage = self.weapon.get_damage() + self.modifier(self.dexterity)
        if damage < 0:
            damage = 0
        actual_damage = target.__take_damage(damage)
        return actual_damage
    
    def should_use_potion(self, enemy: "Character"):
        if self.hp / self.max_hp < 0.3:
            if self.attack(enemy) < enemy.hp:
                return False
            return True
        if self.__buff is None:
            return True
        return False

    def __str__(self):
        return f"{self.name}: {self.hp}/{self.max_hp} HP, Str: {self.strength} ({self.modifier(self.strength)}), Dex: {self.dexterity} ({self.modifier(self.dexterity)}), Weapon: {self.weapon}"

