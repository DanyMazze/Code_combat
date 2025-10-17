from arma import Arma

class Personaggio:
    def __init__(self,nome: str, max_hp: int, forza: int, destrezza: int, arma = None):
        self.__nome = nome
        if max_hp < 1:
            max_hp = 1
        self.__max_hp = max_hp
        self.__hp = max_hp
        if forza < 0:
            forza = 0
        self.__forza = forza
        if destrezza < 0:
            destrezza = 0
        self.__destrezza = destrezza
        self.__arma = arma

    def get_nome(self):
        return self.__nome
    
    def get_max_hp(self):
        return self.__max_hp
    
    def get_hp(self):
        return self.__hp
    
    def get_forza(self):
        return self.__forza
    
    def get_destrezza(self):
        return self.__destrezza
    
    def get_arma(self):
        return self.__arma
    
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_forza(self, forza: int):

        if forza < 0:
            forza = 0
        self.__forza = forza

    def set_destrezza(self, destrezza: int):
        if destrezza < 0:
            destrezza = 0
        self.__destrezza = destrezza

    def equip(self, new_arma: Arma):
        """Equiapaggia una nuova arma al personaggio.
        """
        self.__arma = new_arma

    def modificatore(self, valore: int) -> int:
        return (valore - 10) // 2
    
    def is_alive(self) -> bool:
        return self.__hp > 0
    
    def take_damage(self, damage: int) -> int:
        """Ritorna il danno subito dal personaggio.

            arg damage: danno subito
            return: danno effettivo subito"""
        if damage >= self.__hp:
            damage = self.__hp
        self.__hp -= damage
        return damage
    
    def attacca(self, bersaglio: "Personaggio"):
        """Ritorna il danno effettivo inflitto al bersaglio.
            
            arg bersaglio: Personaggio che riceve l'attacco
            return: danno effettivo inflitto"""
        if self.__arma == None:
            danno =  1
        else:
            if self.__arma.get_tipo() == "mischia":
                danno = self.__arma.get_danno() + self.modificatore(self.__forza)
            elif self.__arma.get_tipo() == "distanza":
                danno = self.__arma.get_danno() + self.modificatore(self.__destrezza)
        if danno < 0:
            danno = 0
        danno_effettivo = bersaglio.take_damage(danno)
        return danno_effettivo

    def __str__(self):
        return f"{self.__nome}: {self.__hp}/{self.__max_hp} HP, For: {self.__forza} ({self.modificatore(self.__forza)}), Des: {self.__destrezza} ({self.modificatore(self.__destrezza)}), Arma: {self.__arma}"
