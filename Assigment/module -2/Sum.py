a=int(input("Enter the first Number  : "))
b=int(input("Enter the Second Number :"))
c=int(input("Enter the Third Number  :"))

if a==b or b==c or c==a:
    print("Sum is 0 because two of the three values are equal.")
else:
    print("sum is :",a+b+c)
