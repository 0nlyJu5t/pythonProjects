import random

exit = False
pcPoints = 0
userPoints = 0
draws = 0

while exit == False:
    options = ["rock","paper","scissors"]
    userInput = input("\nchoose rock, paper, scissors or exit: ")
    computerInput = random.choice(options)
    
    if userInput == "exit":
        print("-Game ended")
        print("\npoints-------------")
        print(f"User:     {userPoints}")
        print(f"Computer: {pcPoints}")
        print(f"Draws:    {draws}")
        exit = True  
        
    if userInput == "rock":
        print(f"Computer: {computerInput}")
        if computerInput == "paper":
            print("-You lose")
            pcPoints+=1
        elif computerInput == "scissors":
            print("-You win")
            userPoints+=1
        else:
            print("-Draw")
            draws+=1
    elif userInput == "paper":
        print(f"Computer: {computerInput}")
        if computerInput == "scissors":
            print("-You lose")
            pcPoints+=1
        elif computerInput == "rock":
            print("-You win")
            userPoints+=1
        else:
            print("-Draw")
            draws+=1
    elif  userInput == "scissors":
        print(f"Computer: {computerInput}")
        if computerInput == "rock":
            print("-You lose")
            pcPoints+=1
        elif computerInput == "paper":
            print("-You win")
            userPoints+=1
        else:
            print("-Draw")
            draws+=1
