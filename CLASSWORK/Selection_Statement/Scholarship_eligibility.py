'''SCHOLARSHIP ELIGIBILITY'''
#Taking percentage as an input
student_perc=float(input('Enter Student percentage:'))
#Validating Student's percentage
if student_perc<=0:
    exit("Student percentage cannot be negative or zero")
if student_perc<=90:
    print("Scholarship Approved!")
else:
    print("Scholarship not Approved!")
-----------------OUTPUT------------------------------------------
Enter Student percentage:87
Scholarship Approved!

=== Code Execution Successful ===
