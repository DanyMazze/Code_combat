from personaggio import Character
from arma import Weapon
import time as t

if __name__ == "__main__":
    character1 = Character("Mario", 100, 12, 12)
    character2 = Character("Luigi", 100, 12, 18)

    sword = Weapon(1, 8, "Long Sword", "melee")
    bow = Weapon(1, 6, "Short Bow", "ranged")
    character1.equip(sword)
    character2.equip(bow)

    print(character1)
    print(character2)

    while character1.is_alive() and character2.is_alive():
        print("A new turn begins!")
        t.sleep(5)
        damage = character1.attack(character2)
        print(f"{character1.name} attacks {character2.name} and deals {damage} damage.")
        print(character2, end="\n\n")
        if not character2.is_alive():
            print(f"{character2.name} has been defeated!")
            break

        damage = character2.attack(character1)
        print(f"{character2.name} attacks {character1.name} and deals {damage} damage.")
        print(character1, end="\n\n")
        if not character1.is_alive():
            print(f"{character1.name} has been defeated!")
            break