from weapon import Weapon
from character import Character
from potion import Potion
from random import randint
from random import choice
from time import sleep

def create_character(potion_health: Potion, potion_strength: Potion, potion_dextrety: Potion) -> object:
    names = ["mario", "luigi", "sara", "thomas"]
    weapons = [Weapon("arco", "ranged", 1, 6), Weapon("spada", "melee", 1, 8)]
    buff_potion = choice([potion_strength, potion_dextrety])
    return Character(choice(names), randint(90,100), randint(10,20), randint(10,20), choice(weapons), [potion_health, potion_health, buff_potion])

if __name__ == "__main__":
    potion_health = Potion("health potion", "health", "hp", 15, 0)
    potion_strength = Potion("strength potion", "buff", "strength", 4, 3) 
    potion_dextrety = Potion("dextrety potion", "buff", "dextrety", 4, 3)  
    
    turn = 0
    player1_buff_durations = []
    player2_buff_durations = []
    
    player1 = create_character(potion_health, potion_strength, potion_dextrety)
    player2 = create_character(potion_health, potion_strength, potion_dextrety)
    print(player1)
    print(player2)

    while player1.is_alive() and player2.is_alive():
        turn += 1
        print(f"--Turn:{turn}--")
        
        potion_used = False
        if player1.should_use_potion() == "health" and player1.have_potion(potion_health):
            player1.use_potion(potion_health)
            print(f"{player1.name} use '{potion_health.name}' now have hp:{player1.hp}")
            potion_used = True
        elif player1.should_use_potion() == "buff" and player1.have_potion(potion_strength):
            duration = player1.use_potion(potion_strength)
            player1_buff_durations.append(duration) 
            print(f"{player1.name} use '{potion_strength.name}' now have str:{player1.strength}")
            potion_used = True
        elif player1.should_use_potion() == "buff" and player1.have_potion(potion_dextrety):
            duration = player1.use_potion(potion_dextrety)
            player1_buff_durations.append(duration) 
            print(f"{player1.name} use '{potion_dextrety.name}' now have dex:{player1.dextrety}")
            potion_used = True

        damage = player1.attack(player2)
        print(f"{player1.name} attack {player2.name}: deal {damage} damage \n")

        potion_used = False
        if player2.should_use_potion() == "health" and player2.have_potion(potion_health):
            player2.use_potion(potion_health)
            print(f"{player2.name} use '{potion_health.name}' now have hp:{player2.hp}")
            potion_used = True
        elif player2.should_use_potion() == "buff" and player2.have_potion(potion_strength):
            duration = player2.use_potion(potion_strength)
            player2_buff_durations.append(duration)  
            print(f"{player2.name} use '{potion_strength.name}' now have str:{player2.strength}")
            potion_used = True
        elif player2.should_use_potion() == "buff" and player2.have_potion(potion_dextrety):
            duration = player2.use_potion(potion_dextrety)
            player2_buff_durations.append(duration)  
            print(f"{player2.name} use '{potion_dextrety.name}' now have dex:{player2.dextrety}")
            potion_used = True

        damage = player2.attack(player1)
        print(f"{player2.name} attack {player1.name}: deal {damage} damage \n")

        print(player1)
        print(player2, "\n")

        expired_buffs = 0
        for i in range(len(player1_buff_durations)):
            player1_buff_durations[i] -= 1
            if player1_buff_durations[i] <= 0:
                expired_buffs += 1
        
        if expired_buffs > 0:
            player1.tick_buff()
            print(f"{player1.name} lose the potion effect")
            player1_buff_durations = [d for d in player1_buff_durations if d > 0]

        expired_buffs = 0
        for i in range(len(player2_buff_durations)):
            player2_buff_durations[i] -= 1
            if player2_buff_durations[i] <= 0:
                expired_buffs += 1
        
        if expired_buffs > 0:
            player2.tick_buff()
            print(f"{player2.name} lose the potion effect")
            player2_buff_durations = [d for d in player2_buff_durations if d > 0]

        sleep(5)