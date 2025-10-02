from arma import Arma

class Personaggio:
    def __init__(self,nome: str, max_hp: int, forza: int, destrezza: int, arma = None):
        self.nome = nome
        if max_hp < 1:
            max_hp = 1
        self.max_hp = max_hp
        self.hp = max_hp
        if forza < 0:
            forza = 0
        self.forza = forza
        if destrezza < 0:
            destrezza = 0
        self.destrezza = destrezza
        self.arma = arma

    def equip(self, new_arma: Arma):
        self.arma = new_arma

    def modificatore(self, valore: int) -> int:
        return (valore - 10) // 2
    
    def is_alive(self) -> bool:
        return self.hp > 0
    
    def take_damage(self, damage: int) -> int:
        if damage >= self.hp:
            damage = self.hp
        self.hp -= damage
        return damage
    
    def attacca(self, bersaglio: "Personaggio"):
        if self.arma == None:
            danno =  1
        else:
            if self.arma.tipo == "mischia":
                danno = self.arma.get_danno() + self.modificatore(self.forza)
            elif self.arma.tipo == "distanza":
                danno = self.arma.get_danno() + self.modificatore(self.destrezza)
        if danno < 0:
            danno = 0
        danno_effettivo = bersaglio.take_damage(danno)
        return danno_effettivo

    def __str__(self):
        return f"{self.nome}: {self.hp}/{self.max_hp} HP, For: {self.forza} ({self.modificatore(self.forza)}), Des: {self.destrezza} ({self.modificatore(self.destrezza)}), Arma: {self.arma}"

