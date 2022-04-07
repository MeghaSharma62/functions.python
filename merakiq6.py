# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))


# def say_hello(name):
#         print("Hello", name)
#         print("How are you?")
# say_hello("Aatif")







# fibbonaci series in recursion



def fibo(n):
        if n==1:
                return 0
        if n==2:
                return 1
        n=int(input("Enter no of terms"))
        for i in range(1,n+1):
                print(fibo(i))
fibo(3)
        