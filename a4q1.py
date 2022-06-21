#Question 1
#To tell the grade of the user

#First we take marks of the user as input
marks=int(input("Enter your marks: "))

if marks>80:
    print(f"Your marks are {marks} and corresponding grade is A")
elif marks>60 and marks<=80:
    print(f"Your marks are {marks} and corresponding grade is B")
elif marks>50 and marks<=60:
    print(f"Your marks are {marks} and corresponding grade is C")
elif marks>45 and marks<=50:
    print(f"Your marks are {marks} and corresponding grade is D")
elif marks>25 and marks<=45:
    print(f"Your marks are {marks} and corresponding grade is E")
elif marks<=25:
    print(f"Your marks are {marks} and corresponding grade is F")
