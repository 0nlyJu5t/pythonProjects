import random

i = 0
nRange = int(input("How big do you want the range of numbers be? 0 - "))

number = random.randint(0,nRange)

while True:
    i += 1
    n = input("\nType a number: ")
    if n.isdigit():
        n = int(n)
    else:
        print("type a number the next time")
        continue
        
    if n == number:
        print(f"\n¡Great, the number was {number}!")
        print(f"You finded the number in {i} tries")
        break
    elif n > number:
        print(f"\n~The number is smaller than {n}")
    else:
        print(f"\n~The number is bigger than {n}")




