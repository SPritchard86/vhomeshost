"""
Program to count people viewing a property.
Author: Stephen Pritchard
Date: 1/07/2019
"""

from customer import Customer
import datetime

REPORT_DAYS = ["Sunday", "Tuesday"]
CURRENT_WEEK_FILE = "customers.csv"

def main():
    casual_customer_count = 0
    casual_view_times = []
    build_customer_count = 0
    build_view_times = []
    print("--- Host Companion App ---")
    print_menu(casual_customer_count, build_customer_count)
    menu_choice = int(input(">>> "))

    while menu_choice != 6:
        if menu_choice == 1:
            casual_customer_count += 1
            casual_view_times.append(get_current_time())
            pass
        elif menu_choice == 2:
            build_customer_count += 1
            build_view_times.append(get_current_time())
        elif menu_choice == 3:
            print("Casual/renovation customer view times: ")
            print(casual_view_times)
            print("Potential build customer view times:")
            print(build_view_times)
        elif menu_choice == 4:
            print_customer_menu()
            cust_menu_choice = int(input(">>> "))
            while cust_menu_choice != 4:
                if cust_menu_choice == 1:
                    create_customer()
                elif cust_menu_choice == 2:
                    pass
                elif cust_menu_choice == 3:
                    pass
                else:
                    print("Invalid option")
                print_customer_menu()
                cust_menu_choice = int(input(">>> "))

        elif menu_choice == 5:
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
    print("Current potential 6-12 months build customer count: {}".format(build_count))
    print("________________MENU________________")
    print("1. Count casual customer")
    print("2. Count potential build customer")
    print("3. View entry times")
    print("4. Customer details")
    print("5. Send weekly report")
    print("6. save and exit")


def print_customer_menu():
    print("__________CUSTOMER DETAILS__________")
    print("1. Add new customer")
    print("2. Edit customer details")
    print("3. Remove customer")
    print("4. Return to main menu")

def get_current_time():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%X")

def create_customer():
    fname = input("First name: ")
    lname = input("Last name: ")
    address = input("Address: ")
    mobile_phone = input("Phone number(M): ")
    work_phone = input("Phone number(W): ")
    home_phone = input("Phone number(H): ")
    home_fax = input("Fax number(H): ")
    work_fax = input("Fax number(W): ")
    email = input("Email address: ")
    house_land_budget = input("Budget (House + Land): ")
    house_only_budget = input("Budget (House only): ")
    is_selling_existing = input("Must sell existing house(Y/N): ")
    if is_selling_existing.lower() == "y":
        is_selling_existing = True
    else:
        is_selling_existing = False
    land_details = input("Land details: ")
    notes = input("notes: ")
    return Customer(fname, lname, address, mobile_phone, work_phone, home_phone, home_fax, work_fax, email, house_land_budget, house_only_budget, is_selling_existing, land_details, notes)



main()

