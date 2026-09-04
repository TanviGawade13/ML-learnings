# 💰 Personal Finance Tracker

A simple CLI-based Personal Finance Tracker built using Python.

This was a project I built mainly to **learn Python by actually building something instead of only watching tutorials or solving isolated questions**.

## What it can do

* Add income and expenses
* View all transactions
* View financial summary and balance
* View category-wise income and expenses
* Search transactions by category
* Delete transactions
* Save transactions to a CSV file
* Load previous transactions when the program starts

## Things I learned while building this

* Functions and program flow
* `while True`, `break`, `continue`, and `return`
* Input validation using `try` and `except`
* Lists and dictionaries working together
* Iterating through dictionaries
* `enumerate()` and `.items()`
* File handling
* Working with CSV files using `DictReader` and `DictWriter`
* Saving and loading data
* Handling edge cases

## Things I got stuck on 🐛

While building this project, I ran into a few bugs:

* My category summary kept increasing every time I viewed it because I was storing the summary dictionaries globally.
* I accidentally placed a `return` outside an `if` block, causing my delete function to exit immediately.
* I called my main program twice, which caused the menu flow to behave incorrectly.
* I had to figure out how CSV data is loaded as strings and convert the `amount` back to a `float`.
* I learned that saving data only when exiting could lead to data loss if the program unexpectedly stopped.

## Biggest takeaway

The most challenging part wasn't writing Python syntax. It was understanding how the data moves through the program:

```text
User Input
    ↓
Validation
    ↓
Transaction Dictionary
    ↓
Transactions List
    ↓
CSV File
    ↓
Program Restart
    ↓
Load CSV Back Into Transactions List
```

This project helped me understand how different Python concepts work together in a real program.

## Tech Used

* Python
* Built-in `csv` module

## Next Improvements

* Add dates to transactions
* Edit transactions
* Monthly summaries
* Data visualization
* Store data using SQLite

---

Built as part of my **project-based Python learning journey** 🚀
