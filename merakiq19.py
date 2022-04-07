# Define a function that checks the speed of drivers. This function will take a
# parameter named speed, and will satisfy the following conditions:
# 1.If speed if less than 70, print 70.
# 2.If speed is more than 70, give 1 point per 5km.(NOTE:This won't count 70).
# 3. If points are more than 12, print “License suspended”


def drive(a):
        if a<=70:
                print("70")
        elif a>70:
                n=(a-70)//5
                if n<12:
                        print(n)
                else:
                        print("license suspended")
a=int(input("Enter the number"))
drive(a)




# n=int(input("enter the number"))
# if n<=70:
#         print("70")
# if n>70:
#         a=(n-70)//5
#         if n<12:
#                 print(n)
#         else:
#                 print("licence suspended")

 