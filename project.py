from tabulate import tabulate
import csv


class Account:


    @classmethod
    def access(cls, key, tablestyle):
        match key:
            case "v":
                try:
                    print(Account.view_expenses(tablestyle))
                except FileNotFoundError:
                    print("Please record an expense first")
            case "a":
                Account.add_expenses()
            case "e":
                Account.edit_expenses()
        

    @classmethod
    def view_expenses(cls, tablestyle):
        table = []
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append({"item": row["item"], "amt": row["amt"], "date": row["date"]})
        headers = {"item": "Item", "amt": "Amount Spent", "date": "Date"}
        if table == []:
            headers = ["Item", "Amount Spent", "Date"]
        return tabulate(table, headers, tablefmt=tablestyle)


    @classmethod
    def add_expenses(cls):
        item = input("Item: ")
        amt = input("Amount spent: ")
        date = input("Date: ")
        with open("expenses.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["item", "amt", "date"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow({"item": item, "amt": amt, "date": date})


    @classmethod
    def edit_expenses(cls):
        item_change = input("Item to be edited: ")
        table = []
        try:
            with open("expenses.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    table.append({"item": row["item"], "amt": row["amt"], "date": row["date"]})
            for index, row in enumerate(table):
                if row["item"] == item_change:
                        del table[index]
            print("Enter new details:")
            item = input("Item: ")
            amt = input("Amount spent: ")
            date = input("Date: ")
            with open("expenses.csv", "w") as file:
                writer = csv.DictWriter(file, fieldnames=["item", "amt", "date"])
                if file.tell() == 0:
                    writer.writeheader()
                writer.writerow({"item": item, "amt": amt, "date": date})
                for row in table:
                    writer.writerow({"item": row["item"], "amt": row["amt"], "date": row["date"]})
        except FileNotFoundError:
            print("Item does not exist")

tablestyle = "rounded_outline"   

def main():
    try:
        tablestyle = customise()
        while True:
            default(tablestyle)
    except EOFError:
        print("\nSuccessfully exited program")
        return 0


def default(tablestyle):
    print(menu(tablestyle))
    print("Ctrl + D to exit program")
    Account.access(input("Enter a key: ").lower(), tablestyle)
    return 0


def menu(tablestyle="rounded_outline"):
        headers = ["Key", "Action"]
        table = [["V", "View Expenses"], ["A", "Add Expenses"], ["E", "Edit Expenses"]]
        return tabulate(table, headers, tablefmt=tablestyle)


def customise():
    tablestyle = input("Enter a suitable table style (Optional): ")
    if tablestyle:
        return tablestyle
    else:
        return "rounded_outline"


if __name__ == "__main__":
    main()