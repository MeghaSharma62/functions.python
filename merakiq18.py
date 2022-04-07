# Define a function which takes one parameter(positive integer). This function returns 
# the sum of all multiples of 3 and 5 (not neccessary common multiples)
# in the range 1 to the integer passed as the parameter.


# def loop():
#         i=0
#         sum=0
#         while i:
#                 if i%3==0 or i%5==0:
#                         print(i)
#                         sum=sum+i
#                 i+=1
#         print(sum)
# # positive=int(input("Enter the number"))
# loop()




# a=int(input("enter the number"))
# i=0
# s=0
# while a>i:
#         s+=int(a)**3
#         if s==a:
#         # i=i+1
# # if n==s:
#                 print("amstrong")
#         else:
#                 print("not")
#         i+=1


# num=int(input("enter the number"))
# l=len(str(num))
# l=int(l)
# a=num
# sum=0
# while num>0:
#         sum+=(num%10)**3
#         num//=10
# if a==sum:
#         print("amstrong")
# else:
#         print("not")


# num=int(input("enter the number"))
# i=0
# a=num
# sum=0
# while num>0:
#         i=num%10
#         sum+=i
#         num//=10
# if a%sum==0:
#         print("harshad")
# else:
#         print("not")


a=int(input("enter the num"))
i=1
count=0
while a>=i:
        if a%i==0:
                print(i)
                count+=1
        i=i+1
if count==2:
        print("prime")
else:
        print("not")

