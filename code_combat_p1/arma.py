from random import randint

class Arma:
    def __init__(self, min_damage: int, max_damage: int, nome: str, tipo: str):
        if min_damage < 0:
            min_damage = 0
        if min_damage > max_damage:
            max_damage = min_damage + 1
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__nome = nome
        if tipo == "mischia" or tipo == "distanza":
            tipo = tipo
        else:
            tipo = "mischia"
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def get_nome(self):
        return self.__nome

    def get_min_danno(self):
        return self.__min_damage

    def get_max_danno(self):
        return self.__max_damage
    
    def set_nome(self, nome: str):
        self.__nome = nome
    
    def set_tipo(self, tipo: str):
        if tipo == "mischia" or tipo == "distanza":
            self.__tipo = tipo
        else:
            self.__tipo = "mischia"
    
    def set_danno(self, min_damage: int, max_damage: int):
        if min_damage < 0:
            min_damage = 0
        if min_damage > max_damage:
            max_damage = min_damage + 1
        self.__min_damage = min_damage
        self.__max_damage = max_damage

    def get_danno(self):
        return randint(self.__min_damage, self.__max_damage)

    def __str__(self):
        return f"{self.__nome} ({self.__tipo}): {self.__min_damage}-{self.__max_damage} danno"
