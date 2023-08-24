# Write a Python program to get the Factorial number of given number.

d = int(input("Enter a Number :"))

fac = 1
if d<0:
    print("Factors do not exist for negative numbers.")
elif d==0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1,d+1):
        fac=fac*i
        print("The factorial of",d,"is",fac)