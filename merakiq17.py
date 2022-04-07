# Define a function which takes one argument which is the limit upto which the 
# function has to print the numbers and their label(even or odd) as shown below.

# Input:-
# 3
# Output :-
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD

def eve(a):
        i=0
        while i<=a:
                if i%2==0:
                        print(i,"odd number")
                else:
                        print(i,"even number")
                i+=1
a=int(input("Enter the number:"))
eve(a)
