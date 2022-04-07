# Q14.Write a function to check if a number is prime or not.


def prim():
        n=int(input("Enter the number:"))
        i=1
        count=0
        while i<=n:
                if n%i==0:
                        count+=1
                i+=1
        if count==2:
                print("prime number")
        else:
                print("not prime number")
prim()
