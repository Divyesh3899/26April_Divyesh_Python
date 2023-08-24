# How will you set the starting value in generating random numbers?


import random

y = "y"
while y!="n":
    random.seed(10)
    print(random.random())
    y=input("Do You Wan't to Countinue 'y' for 'yes' 'n' for 'no' :-")
    