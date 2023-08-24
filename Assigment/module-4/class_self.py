#How to Define a Class in Python? What Is Self? 
# Give An Example Of A Python Class..!



'''In object-oriented programming, whenever we define methods for a class, 
 we use self as the first parameter in each case.'''

class student:
    id=2
    nm='Divyesh'

    def getdata(self):
        print("This is Student Class.")

# Objcet 
st=student()
print(st.id)
print(st.nm)
st.getdata()
