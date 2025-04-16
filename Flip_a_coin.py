import random
from random import randint

print("Welcome to flip a coin game")
choose=input("Pleas choose either heads or tails\n")
ran=randint(1,10)
if(ran%2==0):
    if choose.lower()=="heads" or choose.lower()=="head":
        print("It's heads")
        print("Congratulations You Won!!")
    elif choose.lower()=="tails" or choose.lower()=="tail":
        print("Sorry you lost!!")
    else:
        print("Please enter heads or tails only")
elif(ran%2==1):
    if choose.lower() == "tails" or choose.lower() == "tail":
        print("It's tails")
        print("Congratulations You Won!!")
    elif choose.lower() == "heads" or choose.lower() == "head":
        print("Sorry you lost!!")
    else:
        print("Please enter heads or tails only")
