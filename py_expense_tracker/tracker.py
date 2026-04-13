import csv
import sys
import os

FILE_NAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as x:
            writer = csv.writer(x)
            writer.writerow(["Description", "Amount"])

def add_expense(description, amount):
    init_file()
    with open(FILE_NAME, "a", newline="") as x:
        writer = csv.writer(x)
        writer.writerow([description, amount])
    print(f"Added expense: {description} for ${amount}")

def list_expenses():
    init_file()
    total = 0.0
    print("\n--- Current Expenses ---")
    with open(FILE_NAME, "r") as x:
        reader = csv.reader(x)
        next(reader)  # Skip header
        for row in reader:
            if not row: continue
            desc, amt = row
            total += float(amt)
            print(f"- {desc}: ${amt}")
    print(f"------------------------\nTotal: ${total:.2f}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python tracker.py add <description> <amount>")
        print("  python tracker.py list")
        sys.exit(1)

    command = sys.argv[1].lower()
    
    if command == "add":
        if len(sys.argv) < 4:
            print("Usage: python tracker.py add <description> <amount>")
        else:
            add_expense(sys.argv[2], sys.argv[3])
    elif command == "list":
        list_expenses()
    else:
        print("Unknown command. Valid commands: add, list")
