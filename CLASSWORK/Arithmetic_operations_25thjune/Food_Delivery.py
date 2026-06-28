# Food Delivery Business Profit Analysis

# 1. Taking all inputs from the user
num_orders = int(input("Enter Number of orders: "))
price_per_order = float(input("Enter Price per order: "))
daily_expenses = float(input("Enter Daily expenses: "))
total_food_packets = int(input("Enter Total food packets: "))
packets_per_box = int(input("Enter Packets per box: "))
num_days = int(input("Enter Number of days for prediction: "))

print("\n--- Analysis Output ---")

# 2. Calculating Total Revenue (Number of orders * Price per order)
total_revenue = num_orders * price_per_order
print(f"Total Revenue: {total_revenue}")

# 3. Calculating Profit (Total Revenue - Daily Expenses)
profit = total_revenue - daily_expenses
print(f"Profit: {profit}")

# 4. Determining complete delivery boxes (Using floor division //)
complete_boxes = total_food_packets // packets_per_box
print(f"Complete Boxes: {complete_boxes}")

# 5. Finding remaining food packets (Using modulo %)
remaining_packets = total_food_packets % packets_per_box
print(f"Remaining Packets: {remaining_packets}")

# 6. Predicting future revenue (Assuming revenue doubles daily)
# Formula: total_revenue * (2 ** num_days)
future_revenue = total_revenue * (2 ** num_days)
print(f"Future Revenue (after {num_days} days): {future_revenue}")

------------------------------------------------------OUTPUT---------------------------------------------------------------------------------------------------
Enter Number of orders: 4
Enter Price per order: 40
Enter Daily expenses: 24
Enter Total food packets: 200
Enter Packets per box: 8
Enter Number of days for prediction: 5

--- Analysis Output ---
Total Revenue: 160.0
Profit: 136.0
Complete Boxes: 25
Remaining Packets: 0
Future Revenue (after 5 days): 5120.0

=== Code Execution Successful ===