import random

Attempts = 6

while True:
    bang = random.randint(1,Attempts)
    x = input("shoot? Y/N: ").lower()
    if x == "y":
        if bang != 1:
            print("You are safe")
            Attempts -= 1 
            continue
        else:
            print("You're dead.")
            break
    elif x == "n":
        print("end.")
        break
    else:
        print("type a correct answer")
        continue
        
