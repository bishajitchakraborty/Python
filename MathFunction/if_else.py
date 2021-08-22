marks=int(input("Enter Your Marks:"))
if(marks>=80):
    print("A+")
elif(marks<80 and marks>=70):
    print("A")
elif(marks<70 and marks>=60):
    print("A-")
elif(marks<60 and marks>=50):
    print("B")
elif(marks<50 and marks>=45):
    print("C")
elif(marks<45 and marks>=40):
    print("D")
else:
    print("Fail")

