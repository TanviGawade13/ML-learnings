# personal-finance-tracker

<!-- # break exits a loop 
# return exits a function 
# continue prevents the rest of the code from executing from the current loop 
# .strip() and 
# try except ValueError
# while True
# if not 
# f-strings ----- (f"{variable}sometext{variable}")
# enumerate()
# .items()
# .keys() .values()
# .items() returns a 2d list of tuples 
# for key,value in transaction.items():
# .title()
# iterating over a dictnionry 
so basically python has a inbuilt tool box called csv which helps in operations regarding csv
and in this toolbox there are tools like DictWriter DictReader 
dictwriter converts dictonaries into csv rows -->

Step 1
Import csv module
        ↓
Step 2
Open CSV file with open(filename, 'w', newline="") as csvfile
        ↓
Step 3
Tell Python the column names
        ↓
Step 4
Create a DictWriter 
writer = csv.DictWriter(csvfile, feildnames = column_names) --- here it just tells the dictwriter what the columns are
        ↓
Step 5
Write column headers 
writer.writeheader() actually writes the header in the csv 
        ↓
Step 6
Write every transaction
writer.writer(transactions) ---- transactions is a list containing dictniories
writer.writerows() ---take every dict in the list AND WRITE IN SEPERATE CSV ROW
        ↓
Step 7
Close file automatically

💰 Personal Finance Tracker — Python Only

We will build a CLI-based Personal Finance Tracker first.

<!-- Phase 1 — Error Handling 🛡️ -->
 Handle invalid amount input
 Prevent negative/zero amounts
 Handle empty category
 Handle invalid menu choices
<!-- Phase 2 — Core Features 📋 -->
 View transactions
 Calculate total expenses
 Category-wise spending
 Search/filter transactions
 Delete a transaction
<!-- Phase 3 — File Handling 💾 -->
 Save transactions to CSV
 Load transactions from CSV
 Prevent data loss
<!-- Phase 4 — Final Polish 🚀 -->
 Clean code into functions
 Improve menu
 Test edge cases
 Final project structure