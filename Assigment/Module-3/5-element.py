#Write a Python program to generate and print a list of first and last 5 


list=[]
for i in range(1,31):
    list.append(i**2)
    print(list[:5]+list[-5:])