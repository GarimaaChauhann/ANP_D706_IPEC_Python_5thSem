'''EVENT MANAGEMENT BUDGET'''
#Taking EVENT COST as an input
Event_cost=float(input("Enter Total Event Cost:"))
#Validating EVENT COST 
if Event_cost<=0:
    exit("Event cost cannot be zero or negative")
#Taking Number of Participants as an input
Total_Participants=int(input("Enter total number of participants :"))
#Validating Number of participants
if Total_Participants<=0:
    exit("Total number of Participants can never be zero or negative")
print("Amount per participant :",(Event_cost)/Total_Participants)

-----------------------------------OUTPUT--------------------------------------------------------------------
Enter Total Event Cost:4800
Enter total number of participants :5
Amount per participant : 960.0

=== Code Execution Successful ===