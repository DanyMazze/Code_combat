from personaggio import Personaggio
from arma import Arma
import time as t

if __name__ == "__main__":
    personaggio1 = Personaggio("Mario", 100, 12, 12)
    personaggio2 = Personaggio("Luigi", 100, 12, 18)

    spada = Arma(1, 8, "Spada lunga", "mischia")
    arco = Arma(1, 6, "Arco corto", "distanza")
    personaggio1.equip(spada)
    personaggio2.equip(arco)

    print(personaggio1)
    print(personaggio2)

    while personaggio1.is_alive() and personaggio2.is_alive():
        print("Inizia un nuovo turno!")
        t.sleep(5)
        danno = personaggio1.attacca(personaggio2)
        print(f"{personaggio1.nome} attacca {personaggio2.nome} e infligge {danno} danni.")
        print(personaggio2, end="\n\n")
        if not personaggio2.is_alive():
            print(f"{personaggio2.nome} è stato sconfitto!")
            break

        danno = personaggio2.attacca(personaggio1)
        print(f"{personaggio2.nome} attacca {personaggio1.nome} e infligge {danno} danni.")
        print(personaggio1, end="\n\n")
        if not personaggio1.is_alive():
            print(f"{personaggio1.nome} è stato sconfitto!")
            break