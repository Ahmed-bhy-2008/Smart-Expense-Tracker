print("--- Welcome To XpenseTracker ---")

# 1. Gather inputs
income=float(input("Enter your monthly income in local currency : "))
food_expenses=float(input("How much do you spend monthly on the food : "))
transport_expenses=float(input("How much do you spend monthly on the transport : "))
other_expenses=float(input("How much do you spend monthly on the other matters : "))

# 2. Perform calculations
total_expenses=food_expenses + transport_expenses + other_expenses
savings=income-total_expenses

print("---  Monthly Financial Report ---")
print("your total expenses : ",total_expenses)
print("Net remaining balance: ", savings)

# 3. Analyze savings and provide feedback
if savings > 0:
    saving_percent = (savings / income) * 100
    print(f"Great job! You saved: {savings:.2f}")
    print(f"You managed to save {saving_percent:.1f}% of your total income.")
elif savings == 0:
    print("You broke even this month. Your expenses exactly equal your income.")
    print("Tip: Try to cut down on other matters to start building savings.")
else:
    deficit = abs(savings)
    print(f"Warning: You are overspending! Deficit: -{deficit:.2f}")
    print("You spent more than you earned. Review your expenses to avoid debt.")