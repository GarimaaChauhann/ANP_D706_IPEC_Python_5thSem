'''STUDENT GRADE CALCULATOR'''

# Taking marks as an input (using int as per assignment sample)
student_marks = int(input("Enter Marks: "))

# Validating marks and assigning grades
if student_marks < 0:
    print("Invalid Marks")
elif student_marks >= 90:
    print("Grade A")
elif student_marks >= 75 and student_marks <= 89:
    print("Grade B")
elif student_marks >= 50 and student_marks <= 74:
    print("Grade C")
else:
    print("Grade F")
------------OUTPUT------------------------------------
Enter Marks: 4
Grade F

=== Code Execution Successful ===