import csv
import os
import msvcrt

clear = lambda: os.system('cls')
fieldnames = ["Title", "Type", "Amount", "Date"]

def add_item():
    row = {}

    row[fieldnames[0]] = input("Item title: ")
    row[fieldnames[1]] = input("Is it Income or Expense: ")
    row[fieldnames[2]] = input("Total amount: ")
    row[fieldnames[3]] = input("Transaction date (MM-DD-YYYY): ")

    with open('budgeter.csv',mode="a", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        #writer.writeheader() if file does not exits
        writer.writerow(row)

def total_account_balance():
    income = 0
    expense = 0

    with open('budgeter.csv',mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1]=="Expense":
                expense += int(row[2])
            elif row[1]=="Income":
                income += int(row[2])
        net_balance = income - expense
        print("Net Balance = ", net_balance)

def view_previous_entries():
    with open('budgeter.csv',mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        print(f"{fieldnames[0]}\t{fieldnames[1]}\t{fieldnames[2]}\t{fieldnames[3]}")
        print('-----------------------------')
        for row in csv_reader:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

def select_option():
    print("\nPress any key to continue")
    msvcrt.getch()
    clear()
    print("Select an option:")
    print("1. Add a new entry to the budget tracker")
    print("2. Display the total account balance")
    print("3. View all previous entries")
    print("0. Exit\n")
    choice = input("Option: ")
    print("")
    return choice

choice = ""

while choice != "0":
    choice = select_option()

    if choice == "1":
        add_item()

    elif choice == "2":
        total_account_balance()

    elif choice == "3":
        view_previous_entries()

    elif choice == "0":
        print("Goodbye!")

    else:
        print("Choice not valid. Press 0 to exit.")



