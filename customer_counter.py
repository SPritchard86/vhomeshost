"""
Program to count people viewing a property.
Author: Stephen Pritchard
Date: 1/07/2019
"""


import datetime

REPORT_DAYS = ["Sunday", "Tuesday"]
CURRENT_WEEK_FILE = "customers.csv"

def main():
    casual_customer_count = 0
    casual_view_times = []
    build_customer_count = 0
    build_view_times = []
    print("--- Customer Counter ---")
    print_menu(casual_customer_count, build_customer_count)
    menu_choice = int(input(">>> "))

    while menu_choice != 6:
        if menu_choice == 1:
            casual_customer_count += 1
            casual_view_times.append(get_current_time())
            pass
        if menu_choice == 2:
            pass
        if menu_choice == 3:
            pass
        if menu_choice == 4:
            pass
        if menu_choice == 5:
            pass
        else:
            print("Invalid input")
        print_menu(casual_customer_count, build_customer_count)
        menu_choice = int(input(">>> "))
    print("Goodbye")


def print_menu(casual_count, build_count):
    """Prints the main menu for customer counter"""
    current_datetime = datetime.datetime.now()
    print("Today is {}".format(current_datetime.strftime("%A")))
    if current_datetime.strftime("%A") in REPORT_DAYS:
        print("Today is a reporting day. Make sure to report after 3:30pm!")
    print("Current casual customer count: {}".format(casual_count))
    print("Current potential 0-6m build customer count: {}".format(build_count))
    print("_________MENU__________")
    print("1. Count casual customer")
    print("2. Count potential build customer")
    print("3. view entry times")
    print("4. Take customer details")
    print("5. Send weekly report")
    print("6. save and exit")

def get_current_time():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%X")


main()

