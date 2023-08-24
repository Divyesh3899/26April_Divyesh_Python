#Explain Inheritance in Python with an example?
# What is init? Or What Is A Constructor In Python? 

class Fadher:
    home=0
    bal=0

    def getdata(self):
     self.home=input("Enter car detais:")
     self.bal=input("Enter bank: ")

class Son(Fadher):
    def printdata(self):
        print("Car:",self.home)
        print("Bank Balance:",self.bal)

n=Son()
n.getdata()
n.printdata()




        