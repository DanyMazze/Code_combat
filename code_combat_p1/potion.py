
class Potion:
    def __init__(self, name: str, effect: str, attribute: str, amount: int, duration: int):
        if name == "":
            raise ValueError("name cannot be empty")
        if effect not in ["health", "buff"]:
            raise ValueError("effect must be 'health' or 'buff'")
        if attribute not in ["strength", "dextrety", "hp"]:
            raise ValueError("attribute must be 'strength', 'dextrety' or 'hp'")
        if amount < 1:
            raise ValueError("amount must be >= 1")
        if duration < 1:
            raise ValueError("duration must be >= 1")
        self.__name = name
        self.__effect = effect
        self.__attribute = attribute
        self.__amount = amount
        self.__duration = duration

    @property
    def name(self):
        return self.__name
    
    @property
    def effect(self):
        return self.__effect
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def duration(self):
        return self.__duration
    
    @property
    def attribute(self):
        return self.__attribute
    
    def __str__(self):
        return f"{self.__name}, effect: {self.__effect}, amount: {self.__amount}, duration: {self.__duration}"
    
    # per risolvere il problema di come stanpa le pozioni: 
    def __repr__(self):
        # When a Potion is inside a list, Python uses repr() to display items.
        # Make repr match str so lists of potions print in a readable form.
        return self.__str__()