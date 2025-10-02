from random import randint

class Arma:
    def __init__(self, min_damage: int, max_damage: int, nome: str, tipo: str):
        if min_damage < 0:
            min_damage = 0
        if min_damage > max_damage:
            max_damage = min_damage + 1
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.nome = nome
        if tipo == "mischia" or tipo == "distanza":
            tipo = tipo
        else:
            tipo = "mischia"
        self.tipo = tipo

    def get_danno(self):
        return randint(self.min_damage, self.max_damage)

    def __str__(self):
        return f"{self.nome} ({self.tipo}): {self.min_damage}-{self.max_damage} danno"
