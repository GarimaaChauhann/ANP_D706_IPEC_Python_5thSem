'''MONTHLY SALARY CALCULATOR'''
#Taking  Basic Salary as an input from user
Basic_salary=float(input("Enter Basic salary:"))
#Validating Basic Salary 
if Basic_salary<=0:
    exit("Basic Salary cannot be negative or zero")
#Taking Incentive as an input from the user
Incentive=float(input("Enter Incentive:"))
#Validating Incentive
if Incentive<0:
    exit("Incentive can never be negative")
print("Total Salary is :",(Basic_salary + Incentive))

-----------------OUTPUT-----------------------------------------
Enter Basic salary:58000
Enter Incentive:450
Total Salary is : 58450.0

=== Code Execution Successful ===