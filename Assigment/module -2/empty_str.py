# Write a Python program to get a string made of the first 2 and the last 


a=input("enter string:")
if len(a)>1:
    print(a[0:2]+a[-2:])
else:
    print("Empty String...!")