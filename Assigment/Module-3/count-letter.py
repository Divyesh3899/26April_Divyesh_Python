#Write a Python program to create a dictionary from a string. 

"""output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}"""

str= 'w3resource' 
a = {}
for i in str:
    a[i] = a.get(i, 0) + 1
print(a)