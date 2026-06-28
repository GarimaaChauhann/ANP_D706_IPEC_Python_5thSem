'''ONLINE SHOPPING'''
#Taking product price as an input from user
price=float(input("Enter price:"))
#Validating the price
if price<0:
    exit("price cannot be negative")
#Taking discount amount as an input
discount=float(input("Enter the discount amount:"))
#Validating the discount amount
if discount<0:
    exit("Discount amount cannot be negative")
print("Final Price is :",(price-discount))
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Enter price:5500
Enter the discount amount:400
Final Price is : 5100.0

=== Code Execution Successful ===