import random
print("This is a Dice Stimulator")

x="y"
while x=="y":

    Number =random.randint(1,6)
    if Number==1:
        print("----------")
        print("|        |")
        print("|    0   |")
        print("|        |")
        print("----------")

    if Number==2:
        print("----------")
        print("|        |")
        print("| 0    0 |")
        print("|        |")
        print("----------")

    if Number==3:
        print("----------")
        print("|    0   |")
        print("|    0   |")
        print("|    0   |")
        print("----------")

    if Number==4:
        print("----------")
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")
        print("----------")

    if Number ==5:
        print("----------")
        print("| 0    0 |")
        print("|    0   |")
        print("| 0    0 |")
        print("----------")

    if Number ==6:
        print("----------")
        print("| 0    0 |")
        print("| 0    0 |")
        print("| 0    0 |")
        print("----------")

    x=input("Press y to roll Again And N to Exit")

