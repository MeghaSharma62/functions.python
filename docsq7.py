# Q7.Write function bmi that calculates body mass index 

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"


def bm():
        bmi=int(input("enter the number"))
        if bmi<=18.5:
                print("Underweight")
                return("Underwieght")
        if bmi<=25.0:
                print("Normal")
                return("Normal")
        if bmi<=30.0:
                print("Overweight")
                return("Overweight")
        if bmi>30:
                print("Obese")
                return("Obese")
bm()

