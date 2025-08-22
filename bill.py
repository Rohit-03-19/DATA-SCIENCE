#write a program to create a billing system at supermarket.

while True:
    name = input("enter customer's name: ")
    total = 0

    while True:
        print(" enter the amount and quantity: ")
        amount = float(input("enter the amount : "))
        quantity = float(input("enter the quantity : "))
        total += amount * quantity
        repeat = input("do you want to add more items? (Yes/No): ")
        if repeat == "No" or repeat == "no":
            break
    print ("-"*40)
    print ("Name: ", name)
    print ("Amount to be paid: ", total)
    print ("-"*40)
    print ("*********Happy Shopping*********")
    
    repeat1 = input("Do you want to go to the next customer? (Yes/No) : " )
    if repeat1 == "no" or repeat == "No":
        break