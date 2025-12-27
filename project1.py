import json

FILE_NAME = "expenses.json"

def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_expenses(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

expenses = load_expenses()
monthly_budget = None

print("\nExpense Tracker")

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Category-wise total")
    print("4. Monthly total")
    print("5. Set monthly budget")
    print("6. Edit expense")
    print("7. Delete expense")
    print("8. Import from WhatsApp chat")
    print("9. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ").strip().title()
        date = input("Date (YYYY-MM-DD): ")
        note = input("Note: ")

        expenses.append({
            "amount": amount,
            "category": category,
            "date": date,
            "note": note
        })

        save_expenses(expenses)
        print("Expense added.")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            for i, e in enumerate(expenses, 1):
                print(f"{i}. {e['date']} | {e['cat  egory']} | {e['amount']} | {e['note']}")

    elif choice == "3":
        if not expenses:
            print("No expenses found.")
        else:
            totals = {}
            for e in expenses:
                totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

            for cat, amt in totals.items():
                print(f"{cat}: {amt}")

    elif choice == "4":
        if not expenses:
            print("No expenses found.")
        else:
            monthly = {}
            for e in expenses:
                m = e["date"][:7]
                monthly[m] = monthly.get(m, 0) + e["amount"]

            for m, total in monthly.items():
                print(f"{m}: {total}")
                if monthly_budget and total > monthly_budget:
                    print("Warning: budget exceeded")

    elif choice == "5":
        monthly_budget = float(input("Monthly budget: "))
        print("Budget updated.")

    elif choice == "6":
        if not expenses:
            print("Nothing to edit.")
        else:
            for i, e in enumerate(expenses, 1):
                print(f"{i}. {e['date']} | {e['category']} | {e['amount']} | {e['note']}")

            idx = int(input("Select expense number: ")) - 1

            if 0 <= idx < len(expenses):
                expenses[idx]["amount"] = float(input("New amount: "))
                expenses[idx]["category"] = input("New category: ").strip().title()
                expenses[idx]["date"] = input("New date: ")
                expenses[idx]["note"] = input("New note: ")

                save_expenses(expenses)
                print("Expense updated.")
            else:
                print("Invalid choice.")

    elif choice == "7":
        if not expenses:
            print("Nothing to delete.")
        else:
            for i, e in enumerate(expenses, 1):
                print(f"{i}. {e['date']} | {e['category']} | {e['amount']} | {e['note']}")

            idx = int(input("Select expense number: ")) - 1

            if 0 <= idx < len(expenses):
                removed = expenses.pop(idx)
                save_expenses(expenses)
                print("Deleted:", removed)
            else:
                print("Invalid choice.")

    elif choice == "8":
        path = input("WhatsApp chat file path: ").strip().strip('"')

        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            count = 0

            for line in lines:
                if "Paid ₹" not in line or "]" not in line:
                    continue

                try:
                    date_part = line.split("]")[0].strip("[")
                    d = date_part.split(",")[0]

                    msg = line.split("~:", 1)[1].strip().lower()

                    amount = None
                    for w in msg.split():
                        if w.startswith("₹") and w[1:].replace(".", "", 1).isdigit():
                            amount = float(w[1:])
                            break

                    if amount is None:
                        continue

                    category = "Other"
                    if "swiggy" in msg or "zomato" in msg:
                        category = "Food"
                    elif "uber" in msg or "ola" in msg:
                        category = "Travel"
                    elif "amazon" in msg or "flipkart" in msg:
                        category = "Shopping"

                    day, month, year = d.split("/")
                    date = f"20{year}-{month.zfill(2)}-{day.zfill(2)}"

                    expenses.append({
                        "amount": amount,
                        "category": category,
                        "date": date,
                        "note": msg
                    })

                    count += 1
                except:
                    pass

            save_expenses(expenses)
            print(f"{count} expenses imported.")

        except FileNotFoundError:
            print("File not found.")

    elif choice == "9":
        print("Exiting...")
        break

    else:
        print("Invalid option.")
