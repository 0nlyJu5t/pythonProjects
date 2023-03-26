import random

i = 0
nRange = int(input("How big do you want the range of numbers be? 0 - "))

number = random.randrange(0,nRange)

while True:
    n = int(input("\nEnter a number: "))
    i += 1
    if n == number:
        print(f"\n¡Great, the number was {number}!")
        print(f"You finded the number in {i} tries")
        break
    elif n > number:
        print(f"\n~The number is smaller than {n}")
    elif n < number:
        print(f"\n~The number is bigger than {n}")





