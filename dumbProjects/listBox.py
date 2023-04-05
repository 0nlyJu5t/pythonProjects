myList = []

while True:
    print("\n\nWhat you you want to do with the list? Q to quit")
    print("1-View the list")
    print("2-Add a item")
    print("3-Remove a item")
    print("4-Remove the last item")
    print("5-Insert a item")
    print("6-Sort the items")
    print("7-Clear the list")
    print("8-Exit")

    op = input("Option:")
    if op.isdigit():
        op = int(op)
    else:
        print("\nType a number the next time")
        continue
    
    if op == 1:
        print(f"\n{myList}")
        if not myList:
            print("The list is empty btw")
    elif op == 2:
        n = int(input("\nEnter the data you want to add:"))
        myList.append(n)
    elif op == 3:
        if not myList:
            print("\nThe list is empty")
        else:
            n = input("\nEnter the data you want to remove:")
        myList.remove(n)
    elif op == 4:
        if not myList:
            print("\nThe list is empty")
        else:
            print(f"the data removed was {myList[-1]}")
            myList.pop()
    elif op == 5:
        x = int(input("\nPosition:"))
        n =input("The data:")
        myList.insert(x,n)
    elif op == 6:
        if not myList:
            print("\nThe list is empty")
        else:
            myList.sort()
    elif op == 7:
        if not  myList:
            print("\nThe list is empty")
        else:
            myList.clear()
    elif op == 8:
        quit()
    else:
        print("\nType a number of options for the next time.")