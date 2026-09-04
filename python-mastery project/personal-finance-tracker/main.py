import csv
transactions = []
category_expenses = {}
category_income = {}

def load_csv():
    try:
        filename = 'data.csv'   
        with open(filename , 'r') as csvfile:
            reader = csv.DictReader(csvfile)  #dictreader reads each row and converts it into a dict
            for row in reader: #each row is a dict
                row["amount"] = float(row['amount']) #we convert to float to help in the calculatioins
                transactions.append(row)
            print('Transactions fetched successfully')

    except FileNotFoundError:
        print("The csv file not found")
        return

def save_transaction():
    column_names = ['type','category','amount'] #we use this for the csv to know the order of columns 
    filename = 'data.csv'
    with open(filename, 'w', newline="") as csvfile: #automatically closes the file when the with keyword is used using filename.close() when used file = open(filename)
        writer = csv.DictWriter(csvfile, fieldnames=column_names) #creates a writer object
        writer.writeheader()
        writer.writerows(transactions)
    print("Transactions added to the csv successfully")

def delete_transaction():
    print("\n-------Choose the transaction you want to delete---------")
    for idx ,transaction in enumerate(transactions, start=1):
        print(f"{idx}. {transaction['type']} | {transaction['category']} | {transaction['amount']}")
    try:
        while True: 
            select = int(input("Enter the transaction number you want to delete: ").strip())
            transactions.pop(select-1)
            break

            if not select:
                continue
    except ValueError:
        print("Please enter a valid number")

def search_category():
    category = input("Enter the catergory you want to search : ").strip().title()
    found = False
    for transaction in transactions:
        if transaction['category'] == category:
            print(f"{transaction['type']} | {transaction['category']} | {transaction['amount']}")
            found = True

    if not found:
        print("Transaction not found for this category")

def add_transaction(transaction_type):
    #Amount input validation
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount<=0:
                print("Amount should be more than zero")
                continue
            break
        except ValueError:
            print("Invalid amount inputted")

    #Category input validating 
    while True:
        category = input("Enter the transaction category: ").strip()

        if not category:
            print("The category cannot be Empty")
            continue 
        break


    transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category.title()  #.title() to capitalize each word of the string 
    }
    print(f"Transaction added successfully of amount ${transaction['amount']}")
    transactions.append(transaction)

def view_transaction():
    if len(transactions)==0:
        print("Nothing to show in transactions")
        return

    for i,transaction in enumerate(transactions, start=1):
        print(f"Transaction {i} | {transaction['type']} | {transaction['category']} | {transaction['amount']}")

def view_summary():
    income=0
    expense=0

    for transaction in transactions:
        if transaction["type"] == "Income":
            income+=transaction["amount"]
        elif transaction["type"] == "Expense":
            expense+=transaction["amount"]

    balance = income - expense
    print("\n----- Financial Summary -----")
    print(f"Total Income: ${income}")
    print(f"Total Expense: ${expense}")
    print(f"Current Balance: ${balance}")

def category_summary():
    for transaction in transactions:
        category = transaction['category']
        amount = transaction['amount']
        if transaction['type'] == "Expense":
            if category not in category_expenses:
                category_expenses[category] = amount
            else:
                category_expenses[category]+= amount
        elif transaction['type']== 'Income':
            if category not in category_income:
                category_income[category] = amount
            else:
                category_income[category]+= amount

    if not category_income:
        print("The income category is empty")
    else: 
        print("\n----- CATEGORY-WISE INCOME -----")
        for category,amount in category_income.items():
            print(f"{category}: {amount}")

    if not category_expenses:
        print("The expense category is empty ")
    else:
        print("\n----- CATEGORY-WISE EXPENSES -----")
        for category,amount in category_expenses.items():
            print(f"{category}: {amount}")

def main_prog():
    while True:
        print(
'''
Select one of the following options:
1) Add income
2) Add expenses
3) View all transactions
4) View the financial summary/balance
5) View the category summary
6) Search by category
7) Delete transaction
8) Exit the program
'''
)
        try: 
            
            choice = int(input("Enter your choice: ").strip())

            if choice == 1:
                add_transaction("Income")
            elif choice == 2: 
                add_transaction("Expense")
            elif choice == 3:
                view_transaction()
            elif choice == 4:
                view_summary()
            elif choice == 5:
                category_summary()
            elif choice == 6: 
                search_category()
            elif choice == 7:
                delete_transaction()
            elif choice == 8:
                save_transaction()
                print("Thanks for using personal finance tracker")
                return
            else: 
                print("The value should be a number between 1 to 5")

        except ValueError: 
            print("The value should be a number")

load_csv()
main_prog()