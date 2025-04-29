#Generate sales report for a specific month
import csv

def sales(month: str, amount: float) -> str:
    return f"In the month {month}, a total of {amount} was sold"

#Generate an expense report for a specific month
def expenses(month: str, amount: float):
    record = {
        "Month": month,
        "Expenses": amount
    }

    with open('expense_record.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=record.keys())
        writer.writeheader()
        writer.writerow(record)

    print("EXPENSE FILE CREATED SUCCESSFULLY")
