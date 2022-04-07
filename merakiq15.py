# Perfect Number?
# A perfect number is the one which 
# is equal to the sum of all it's factors(including 1 and excluding itself)

# def perfect():
#         a=int(input("Enter the number"))
#         sum=0
#         i=1
#         while i<a:
#                 if a%i==0:
#                         sum+=i
#                 i+=1
#         if sum==a:
#                 print("perfect number")
#         else:
#                 print("not perfect number")
# perfect()



a=int(input("Enter the number"))
sum=0
i=1
while i<a:
        if a%i==0:
                sum+=i
                i+=1
if sum==a:
        print("perfect number")
else:
        print("not perfect number")



# a=int(input("enter the number"))
# sum=0
# i=1
# while i<a:
#         if a%i==0:
#                 sum=sum+i
#                 i=i+1
# if sum==a:
#         print("perfect number")
# else:
#         print("not perfect number")