# Function to display menu and handle user's choices
def display_menu():
    print("\n====== Income and Expense Manager ======")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Check Balance")
    print("5. Exit")
    print("========================================")

# Function to add income
def add_income(record):
    category = input("Enter income source (e.g., Salary, Freelance, etc.): ")
    amount = float(input(f"Enter income amount for {category}: "))
    
    # If the category exists, add to it; else create a new one
    if category in record["income"]:
        record["income"][category] += amount
    else:
        record["income"][category] = amount
    
    print(f"Income of {amount} added under {category}.")

# Function to add expense
def add_expense(record):
    category = input("Enter expense category (e.g., Rent, Food, etc.): ")
    amount = float(input(f"Enter expense amount for {category}: "))
    
    # If the category exists, add to it; else create a new one
    if category in record["expense"]:
        record["expense"][category] += amount
    else:
        record["expense"][category] = amount
    
    print(f"Expense of {amount} added under {category}.")

# Function to display the summary of all income and expenses
def view_summary(record):
    print("\n===== Income Summary =====")
    total_income = 0
    for category, amount in record["income"].items():
        print(f"{category}: {amount}")
        total_income += amount
    
    print(f"\nTotal Income: {total_income}")
    
    print("\n===== Expense Summary =====")
    total_expense = 0
    for category, amount in record["expense"].items():
        print(f"{category}: {amount}")
        total_expense += amount
    
    print(f"\nTotal Expense: {total_expense}")

# Function to calculate and display the balance
def check_balance(record):
    total_income = sum(record["income"].values())
    total_expense = sum(record["expense"].values())
    balance = total_income - total_expense
    
    print(f"\nTotal Balance: {balance}")
    if balance > 0:
        print("You are in surplus!")
    elif balance < 0:
        print("You are in deficit!")
    else:
        print("Your account is balanced.")

# Main function to manage the program's workflow
def income_expense_manager():
    record = {"income": {}, "expense": {}}  # Initialize dictionary to store income and expenses

    while True:
        display_menu()  # Display menu options
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_income(record)
        elif choice == '2':
            add_expense(record)
        elif choice == '3':
            view_summary(record)
        elif choice == '4':
            check_balance(record)
        elif choice == '5':
            print("Exiting Income and Expense Manager. Goodbye!")
            break
        else:
            print("Invalid input, please choose again.")

# Entry point for the program
if __name__ == "__main__":
    income_expense_manager()
# complete