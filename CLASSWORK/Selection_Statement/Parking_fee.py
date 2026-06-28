'''PARKING FEE WAIVER'''
#Taking Purchase amount as an input
Purchase_amount=float(input("Enter Purchase amount :"))
#Validating the purchase amount
if Purchase_amount<0:
    exit("Purchase amount cannot be negative")
if Purchase_amount>=2000:
    print("Parking Fee Waived!")
    print("Parking Fee : $0")
else:
    print("Parking fee applicable!")
    print("Parking fee:$100")

-------------OUTPUT-----------------------------
Enter Purchase amount :5000
Parking Fee Waived!
Parking Fee : $0

=== Code Execution Successful ===