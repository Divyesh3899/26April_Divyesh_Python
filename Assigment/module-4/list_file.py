#Write a Python program to write a list to a file.

x=open("patel.txt",'a')

list=["My name is Divyesh Kotdia. And I am a software developer. I am also the secretary of Shri Khodaldham Residency."]
x.write('\n')
for i in list:
    x.write(f'{i}\n')