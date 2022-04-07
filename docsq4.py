# Q4.Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".


# def st():
        
def up(a):
        i=0
        count=0
        count1=0
        while i<len(a):
                if a[i]>=chr(65) and a[i]<=chr(90):
                        count+=1
                else:
                        count1+=1
                i+=1
        print("uppercase",count)
        print("lowercase",count1)
up("MegHa")
