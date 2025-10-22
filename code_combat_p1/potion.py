from personaggio import Character

class Potion:
    def __init__(self, name: str, effect: str, amount: int, duration: int):
        self.__name = name
        self.__effect = effect
        self.__amount = amount
        self.__duration = duration

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def effect(self):
        return self.__effect
    @effect.setter
    def effect(self, value: str):
        if value not in ["heal", "buff_strength", "buff_dexterity"]:
            value = "heal"
        self.__effect = value

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, value: int):
        if value < 0:
            value = 0
        self.__amount = value

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, value: int):
        if value < 0:
            value = 0
        self.__duration = value
    
    def use(self, character: "Character"):
        if self.effect == "heal":
            character.heal(self.amount)
        elif self.effect == "buff_strength":
            character.add_buff("strength", self.amount)
        elif self.effect == "buff_dexterity":
            character.add_buff("dexterity", self.amount)
