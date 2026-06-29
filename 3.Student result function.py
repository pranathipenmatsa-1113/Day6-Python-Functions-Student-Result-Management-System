def total_marks(m1, m2, m3, m4, m5):
    return m1 + m2 + m3 + m4 + m5
def average_marks(total):
    return total / 5
def grade(avg):
    if avg >= 90:
        return "GRADE A"
    elif avg >= 80:
        return "GRADE B"
    elif avg >= 70:
        return "GRADE C"
    elif avg >= 60:
        return "GRADE D"
    else:
        return "GRADE E"
def result(m1, m2, m3, m4, m5):
    if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
        return "FAIL"
    else:
        return "PASS"
print("==============================")
print(" STUDENT RESULT MANAGEMENT SYSTEM ")
print("==============================")
name = input("Enter Student Name: ")
m1 = int(input("Enter Maths Marks: "))
m2 = int(input("Enter Science Marks: "))
m3 = int(input("Enter English Marks: "))
m4 = int(input("Enter Social Marks: "))
m5 = int(input("Enter Computer Marks: "))

total = total_marks(m1, m2, m3, m4, m5)
average = average_marks(total)
student_grade = grade(average)
student_result = result(m1, m2, m3, m4, m5)
print("\n==============================")
print("      STUDENT RESULT")
print("==============================")
print("Student Name :", name)
print("Maths        :", m1)
print("Science      :", m2)
print("English      :", m3)
print("Social       :", m4)
print("Computer     :", m5)
print("------------------------------")
print("Total Marks  :", total)
print("Average      :", average)
print("Grade        :", student_grade)
print("Result       :", student_result)
print("==============================")
print("\nCode Generated Successfully....")
input("Press Enter to Exit...")
