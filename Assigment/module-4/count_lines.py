#Write a Python program to count the number of lines in a text file. 

x=open("patel.txt","r")
print(len(x.readlines()))
x.close()