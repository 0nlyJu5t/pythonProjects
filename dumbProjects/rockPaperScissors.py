import random

pcPoints = 0
userPoints = 0
draws = 0
options = ["rock","paper","scissors"]
  
while True:
    userInput = input("\nchoose rock/paper/scissors or Q to quit: ").lower()
    
    if userInput == "q":
        break
        
    if userInput not in options:
        continue
    
    computerInput = random.choice(options)
    print(f"Computer: {computerInput}")
    if userInput == "rock" and computerInput == "scissors":
        print("-You won")
        userPoints+=1
    elif userInput == "paper" and computerInput == "rock":
        print("-You won")
        userPoints+=1
    elif  userInput == "scissors" and computerInput == "paper":
        print("-You won")
        userPoints+=1
    else:
        print("-You lost")
        pcPoints+=1
        
print(f"You won {userPoints} times.")
print(f"the computer won {pcPoints} times.")
        