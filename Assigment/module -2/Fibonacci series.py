ab=int(input("enter a number:"))
e,g=0,1
print("Fibonacci Series:",e,g,end=" ")
for i in range(2,ab):
    z=e+g
    e=g
    g=z
    print(z,end=" ")
print()