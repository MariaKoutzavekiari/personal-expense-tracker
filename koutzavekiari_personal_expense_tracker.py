# Author: Maria Koutzavekiari
# Date: September 17, 2026
# Description: Personal Expense Tracker
# Tier Level: Intermediate Level

import os
import csv
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "expenses.csv")


def load_expenses():
    records = []

    if os.path.exists(FILENAME):
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                records.append(row)

    return records


def save_expenses(records):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)

        for record in records:
            writer.writerow(record)


def add_expense(records):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: $"))

    new_record = [date, category, description, amount]
    records.append(new_record)

    return records


def display_records(records):
    print("\n===== Expense Records =====")

    for record in records:
        print(
            f"Date: {record[0]} | "
            f"Category: {record[1]} | "
            f"Description: {record[2]} | "
            f"Amount: ${float(record[3]):.2f}"
        )

    print("===========================")


def search_expenses(records, keyword):
    matches = []

    for record in records:
        if keyword.lower() in record[1].lower() or keyword.lower() in record[2].lower():
            matches.append(record)

    return matches


def calculate_totals(records):
    totals = []

    for record in records:
        category = record[1]
        amount = float(record[3])
        found = False

        for i in range(len(totals)):
            if totals[i][0] == category:
                new_total = totals[i][1] + amount
                totals[i] = (category, new_total)
                found = True
                break

        if not found:
            totals.append((category, amount))

    totals.sort(key=lambda item: item[1], reverse=True)

    return totals
try:
    records = load_expenses()

    print("Welcome to Personal Expense Tracker")

    display_records(records)

    add_more = input("Would you like to add an expense? (yes/no): ")

    if add_more.lower() == "yes":
       records = add_expense(records)
       save_expenses(records)
       print("Expense added successfully.")
       display_records(records)


    search_choice = input("Would you like to search your expenses? (yes/no): ")

    if search_choice.lower() == "yes":
       keyword = input("Enter a keyword to search: ")
       matches = search_expenses(records, keyword)

       if matches:
        display_records(matches)

       else:
        print("No matching expenses found.")


    totals = calculate_totals(records)

    print("\n===== Spending by Category =====")

    for category, total in totals:
        print(f"{category:<15} ${total:>8.2f}")

    print("===============================")
except Exception as error:
    print(f"An unexpected error occurred: {error}")

finally:
    print("Thank you for using Expense Tracker. Goodbye!")