# Q5.Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].


def un():
        l=[1,2,3,3,3,3,4,5]
        i=0
        b=[]
        while i<len(l):
                if l[i] not in b:
                        b.append(l[i])
                i+=1
        print(b)
un()