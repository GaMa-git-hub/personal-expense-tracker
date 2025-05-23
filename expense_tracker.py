# personal_expense_tracker.py

from datetime import datetime

expenses = []

def get_valid_date(prompt):
    while True:
        date_input = input(prompt)
        try:
            datetime.strptime(date_input, '%Y-%m-%d')
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def add_expense():
    date = get_valid_date("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            break
        except ValueError:
            print("Please enter a valid number for amount.")
    expenses.append({"date": date, "description": description, "amount": amount})
    print("Expense added successfully.\n")

def show_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("\nList of expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['description']} | ₹{expense['amount']:.2f}")
    print()

def show_total():
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal expenses: ₹{total:.2f}\n")

def main():
    while True:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Total")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            show_total()
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.\n")

if __name__ == "__main__":
    main()
