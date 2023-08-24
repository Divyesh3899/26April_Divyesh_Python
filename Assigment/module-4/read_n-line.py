#Write a Python program to read first n lines of a file.

x=open("petel.txt",'a')
x.write('''My name is Divyesh Kotdia
I am also the secretary of Shri Khodaldham Residency.
     I am a software developer.''')
x.close()
x=open("patel.txt",'r')
print(x.readlines()[:5])