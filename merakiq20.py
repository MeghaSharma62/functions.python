# Create a function which takes one argument (a positive integer) and returns a
# dictionary which has numbers from 1 to the integer (passed as parameter)as the keys
# and their respective squares as the values as shown in the examble below.
def sq(a):
        i=0
        while i<=a:
                print(i,i**2)
                i+=1
a=int(input("Enter the number"))
sq(a)








