import random
combat_player = ["Punch", "Kick", "Domain Expansion"]
combat_boss = ["Shadow grab", "Skull crushing blow", "Domain Expansion"]
boss_list = ["Zoltrax", "Akuma", "Shinigami"]
name = input("Please enter your name to start the game: ")
boss = input("Choose your desired boss from 0 to 2: ")
boss = int(boss)
if boss == 0:
    print ("You have chosen Zoltrax to duel, prepare to fight.")
elif boss == 1:
    print ("You have chosen Akuma to fight, prepare to fight.")
elif boss == 2:
    print ("You have chosen Shinigami to fight, prepare to fight.")
else:
    print ("Please choose a valid number.")
