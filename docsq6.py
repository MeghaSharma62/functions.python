# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].


def ex():
        m=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        i=0
        b=[]
        while i<len(m):
                if m[i]%2==0:
                        b.append(m[i])
                i+=1
        print(b)
ex()