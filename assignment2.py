import json
from datetime import datetime

# File to store the data
data_file = 'budget_data.txt'

# Load existing data
def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"income": [], "expenses": []}

# Save data
def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

# Add income
def add_income(source, amount):
    data = load_data()
    data["income"].append({"source": source, "amount": amount, "date": str(datetime.now())})
    save_data(data)

# Add expense
def add_expense(category, amount):
    data = load_data()
    data["expenses"].append({"category": category, "amount": amount, "date": str(datetime.now())})
    save_data(data)

# Calculate remaining budget
def calculate_budget():
    data = load_data()
    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    return total_income - total_expenses

# Main function to interact with the user
def main():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Check Budget")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            source = input("Enter income source: ")
            amount = float(input("Enter amount: "))
            add_income(source, amount)
            print("Income added successfully.")
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            add_expense(category, amount)
            print("Expense added successfully.")
        elif choice == '3':
            print(f"Remaining budget: {calculate_budget()}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
