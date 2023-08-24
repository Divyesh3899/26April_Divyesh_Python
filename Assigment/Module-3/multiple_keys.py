# Write a Python program to check multiple keys exists in a dictionary.

"""import keyword
from tokenize import Name
dict={'id':1,'Name':'Divyesh','Sub':' core python'}

'''s1=set(['id','Name'])
print(s1.issubset(dict.keys())) '''
print(dict.keys()>={'id','Name'})
"""

dic={}
keys=[]
n=int(input("Enter Number Of Swizerland:-"))
for i in range(n):
    key=input("Enter Number Of Key's:-")
    value=input("Enter Number Of Value:- ")
    dic[key]=value
print(dic)

for i in dic.keys():
    keys.append(i)
print(keys)

if len(keys)>1:
    print("Multiple Keys")
else:
    print("not multiple key")