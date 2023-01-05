import random

def numberGenerator():
    return random.randint(1,6)

def printDice(x):
    if(x==1):
        print("[-----------]\n[           ]\n[     0     ]\n[           ]\n[-----------]")
    if(x==2):
        print("[-----------]\n[           ]\n[   0   0   ]\n[           ]\n[-----------]")
    if(x==3):
        print("[-----------]\n[     0     ]\n[     0     ]\n[     0     ]\n[-----------]")
    if(x==4):
        print("[-----------]\n[  0     0  ]\n[           ]\n[  0     0  ]\n[-----------]")
    if(x==5):
        print("[-----------]\n[  0     0  ]\n[     0     ]\n[  0     0  ]\n[-----------]")
    if(x==6):
        print("[-----------]\n[  0     0  ]\n[  0     0  ]\n[  0     0  ]\n[-----------]")

a="y"
while(a=="y"):
    if(a == "y"):
        printDice(numberGenerator())
    a = input("Press y to roll again, and n to stop: ")
