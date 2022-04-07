# Q25. Given a list of numbers, write a Python program to count positive and
# negative numbers in a List using function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3


def ne():
        list1 = [2, -7, 5, -64, -14]
        i=0
        pos=0
        neg=0
        while i<len(list1):
                if list1[i]>0:
                        pos+=1
                else:
                        neg+=1
                i+=1
        print("pos=",pos,"neg=",neg)
ne()