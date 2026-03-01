from datetime import date
import pandas as pd

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.total_spent = 0
        self.load_from_csv()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.total_spent += transaction.amount

    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def get_total_spent(self):
        return self.total_spent

    def export_to_csv(self):
        transactions_data = [obj.__dict__ for obj in self.transactions]
        df = pd.DataFrame(transactions_data)
        df.to_csv('transactions.csv')

    def load_from_csv(self):
        try:
            df = pd.read_csv('transactions.csv')
            for _, row in df.iterrows():
                t = Transaction(row['date'], row['amount'],
                                row['category'], row['description'])
                self.total_spent += t.amount
                self.transactions.append(t)
        except FileNotFoundError:
            pass

    def display_summary(self):
        dict_category = {}
        for i in self.transactions:
            if i.category not in dict_category:
                dict_category[i.category] = i.amount
            else:
                dict_category[i.category] += i.amount

        for category in dict_category.keys():
            print(f"{category}: {dict_category[category]}")

        print(f"Total Spent: {self.total_spent}")

    def display_menu(self):
        print("1. Add transaction.")
        print("2. View transactions.")
        print("3. Export to CSV.")
        print("4. Print Summary.")
        print("5. Exit")

class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return (f"{self.date}, ${self.amount}, {self.category}, "
                f"{self.description}.")

def main():
    obj = BudgetTracker()

    while True:
        obj.display_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                today = date.today()
                amount = float(input("Enter money spent: "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                trans = Transaction(today, amount, category, description)
                obj.add_transaction(trans)
            case "2":
                obj.view_transactions()
            case "3":
                obj.export_to_csv()
            case "4":
                obj.display_summary()
            case "5":
                obj.export_to_csv()
                break

if __name__ == '__main__':
    main()