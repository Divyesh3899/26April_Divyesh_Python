# Write a Python program to append text to a file and display the text.

from fileinput import close


x=open("Divyesh.txt",'a')
x.write("My name is Divyesh Kotdia\n.")
x.close()

y=open("Divyesh.txt",'r')
print(y.read())