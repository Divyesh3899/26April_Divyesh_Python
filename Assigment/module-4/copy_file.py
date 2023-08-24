#Write a Python program to copy the contents of a file to another file.

x=open("patel.txt",'r')
y=open("patel-2.txt",'w')

for i in x:
   y.write(i)