def grade(marks):
    if marks>=90:
        return "GRADE A"
    elif marks>=80:
        return "GRADE B"
    elif marks>=70:
        return "GRADE C"
    elif marks>=60:
        return "GRADE D"
    else:
        return "GRADE E"
    print(marks)
marks=int(input("Enter marks:"))
result=grade(marks)
print("THE GRADE IS:",result)
print("\n--------------------")
print("Code Generate Successfully....")
input("Please Click Enter to Exit")
