from personaggio import Character
from arma import Weapon
from potion import Potion
import time as t

if __name__ == "__main__":
    buff_index_duration_character1 = 0
    buff_index_duration_character2 = 0
    character1 = Character("Mario", 100, 12, 12)
    character2 = Character("Luigi", 100, 12, 18)

    sword = Weapon(1, 8, "Long Sword", "melee")
    bow = Weapon(1, 6, "Short Bow", "ranged")
    character1.weapon = sword
    character2.weapon = bow
    health_potion = Potion("Health Potion", "heal", 20, 0)
    strength_potion = Potion("Ogre Tonic", "buff_strength", 2, 3)
    dexterity_potion = Potion("Cat’s Grace", "buff_dexterity", 2, 3)
    character1.potions.append(health_potion)
    character1.potions.append(health_potion)
    character1.potions.append(strength_potion)  
    character2.potions.append(health_potion)
    character2.potions.append(health_potion)
    character2.potions.append(dexterity_potion)

    print(character1)
    print(character2)

    while character1.is_alive() and character2.is_alive():
        if buff_index_duration_character1 > 0:
            buff_index_duration_character1 -= 1
            if buff_index_duration_character1 == 0:
                character1.tick_buff(buff_attribute_character1, buff_amount_character1)
        if buff_index_duration_character2 > 0:
            buff_index_duration_character2 -= 1
            if buff_index_duration_character2 == 0:
                character2.tick_buff(buff_attribute_character2, buff_amount_character2)
        print("A new turn begins!")
        t.sleep(5)
        potion_decision = character1.should_use_potion(character2)
        if potion_decision != -1:
            for potion in character1.potions:
                if potion_decision == 0 and potion.effect == "heal":
                    potion.use(character1)
                    print(f"{character1.name} uses {potion.name}.")
                    character1.potions.remove(potion)
                    break
                elif potion_decision == 1:
                    buff_index_duration_character1 = potion.duration
                    potion.use(character1)
                    print(f"{character1.name} uses {potion.name}.")
                    buff_attribute_character1 = potion.effect
                    buff_amount_character1 = potion.amount
                    character1.potions.remove(potion)
                    
            
            print(character1, end="\n\n")
            t.sleep(5)
        damage = character1.attack(character2)
        print(f"{character1.name} attacks {character2.name} and deals {damage} damage.")
        print(character2, end="\n\n")
        if not character2.is_alive():
            print(f"{character2.name} has been defeated!")
            break

        potion_decision = character2.should_use_potion(character1)
        if potion_decision != -1:
            for potion in character2.potions:
                if potion_decision == 0 and potion.effect == "heal":
                    potion.use(character2)
                    print(f"{character2.name} uses {potion.name}.")
                    character2.potions.remove(potion)
                    break
                elif potion_decision == 1:
                    buff_index_duration_character2 = potion.duration
                    potion.use(character2)
                    print(f"{character2.name} uses {potion.name}.")
                    buff_attribute_character2 = potion.effect
                    buff_amount_character2 = potion.amount
                    character2.potions.remove(potion)
                    break
            
            print(character2, end="\n\n")
            t.sleep(5)
        damage = character2.attack(character1)
        print(f"{character2.name} attacks {character1.name} and deals {damage} damage.")
        print(character1, end="\n\n")
        if not character1.is_alive():
            print(f"{character1.name} has been defeated!")
            break
