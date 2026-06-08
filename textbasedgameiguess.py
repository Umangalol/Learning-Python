combat = ["Punch", "Kick","Ultimate"]
player_name, HP = input("Enter your player's name and your starting HP: ").split()
HP = int(HP)
print ("Enemy found you, prepare for battle.")
print ("Available moves are as follows:")
print ("-".join(combat))
reply = input("Choose your move: ")
if reply == "Punch":
    print("You punched the enemy, damage dealt 20!")
    print ("Enemy's HP went from 200 to 180")
elif reply == "Kick":
    print("Damage critical! You kicked the enemy and it fled away.")
elif reply == "Ultimate":
    print("Fatality! You win.")
else:
  print("You died. You didn't choose an appropriate move and died by your own stupidity.")
  
  
