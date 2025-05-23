import json
import os
from datetime import datetime

FILE_NAME = 'expenses.json'
expenses = []

def load_expenses():
    global expenses
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            expenses = json.load(f)
    else:
        expenses = []

def save_expenses():
    with open(FILE_NAME, 'w') as f:
        json.dump(expenses, f, indent=4)

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
    save_expenses()
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

def edit_expense():
    show_expenses()
    if not expenses:
        return
    try:
        idx = int(input("Enter the number of the expense to edit: ")) - 1
        if 0 <= idx < len(expenses):
            expense = expenses[idx]
            print(f"Editing expense: {expense}")
            new_date = input(f"New date (YYYY-MM-DD) [{expense['date']}]: ")
            if new_date:
                try:
                    datetime.strptime(new_date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Keeping original date.")
                    new_date = expense['date']
            else:
                new_date = expense['date']

            new_desc = input(f"New description [{expense['description']}]: ") or expense['description']
            while True:
                new_amount_input = input(f"New amount [{expense['amount']}]: ")
                if new_amount_input == '':
                    new_amount = expense['amount']
                    break
                try:
                    new_amount = float(new_amount_input)
                    break
                except ValueError:
                    print("Please enter a valid number.")
            expenses[idx] = {"date": new_date, "description": new_desc, "amount": new_amount}
            save_expenses()
            print("Expense updated successfully.\n")
        else:
            print("Invalid expense number.\n")
    except ValueError:
        print("Invalid input.\n")

def delete_expense():
    show_expenses()
    if not expenses:
        return
    try:
        idx = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= idx < len(expenses):
            deleted = expenses.pop(idx)
            save_expenses()
            print(f"Deleted expense: {deleted}\n")
        else:
            print("Invalid expense number.\n")
    except ValueError:
        print("Invalid input.\n")

def main():
    load_expenses()
    while True:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Show Total")
        print("4. Edit Expense")
        print("5. Delete Expense")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            show_total()
        elif choice == '4':
            edit_expense()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.\n")

if __name__ == "__main__":
    main()
