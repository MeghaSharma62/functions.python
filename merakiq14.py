# If user's age is less than 18 , print “not eligible “,
# else if user's age is greater than or equal to 18, print “you are eligible”.

def vote():
        age=int(input("Enter the number"))
        if age<18:
                print("not eligile to vote")
        else:
                print("Eligible to vote")
vote()