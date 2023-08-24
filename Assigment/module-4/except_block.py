#Can one block of except statements handle multiple exception?

a=0
b=0
try:
    print(a/b)
except:
    print('Error..')
    print("can't divide by 0")