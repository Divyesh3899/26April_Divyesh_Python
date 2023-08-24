# Write a Python program to remove duplicates from a list. 

"""a=['Divyesh','Nirav','chandni','bhavik','Nidhi','Yasvi','Gopi']
print(a)
a.remove("Gopi")
print(a)"""

a=[]
n=int(input("Enter number of student's:"))
for i in range(n):
    x=input("Enter your name:")
    a.append(x)
    a=list(set(a))
print("Remove duplicates list : ",a)
