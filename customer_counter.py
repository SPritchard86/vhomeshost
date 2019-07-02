"""
Program to count people viewing a property.
Author: Stephen Pritchard
Date: 1/07/2019
"""

from customer import Customer
import datetime

REPORT_DAYS = ["Sunday", "Tuesday"]
REPORT_EMAILS = ["stephen.pritchard@my.jcu.edu.au"]
CURRENT_WEEK_FILE = "customers.csv"


def main():
    casual_customer_count = 0
    casual_view_times = []
    build_customer_count = 0
    build_view_times = []
    customers = []
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
            list_customers(customers)
            print_customer_menu()
            cust_menu_choice = int(input(">>> "))
            while cust_menu_choice != 5:
                list_customers(customers)
                if cust_menu_choice == 1:
                    if len(customers) >= 1:
                        try:
                            customer = int(input("Enter customer number: "))
                            print("Name: {} {}".format(customers[customer - 1].fname, customers[customer - 1].lname))
                            print("Address: {}".format(customers[customer - 1].address))
                            print("Ph(Mobile): {}".format(customers[customer - 1].mobile_phone))
                            print("Ph(Work): {}".format(customers[customer - 1].work_phone))
                            print("Ph(Home): {}".format(customers[customer - 1].home_phone))
                            print("Fax(Home): {}".format(customers[customer - 1].home_fax))
                            print("Fax(Work): {}".format(customers[customer - 1].work_fax))
                            print("Email: {}".format(customers[customer - 1].email))
                            print("House/Land budget: {}".format(customers[customer - 1].house_land_budget))
                            print("House only budget: {}".format(customers[customer - 1].house_only_budget))
                            print("Is Selling existing: {}".format(customers[customer - 1].is_selling_existing))
                            print("Land details: {}".format(customers[customer - 1].land_details))
                            print("Notes: {}".format(customers[customer - 1].notes))
                        except IndexError:
                            print("Invalid customer")
                        except ValueError:
                            print("Enter a valid number.")
                    else:
                        print("No customers stored")


                elif cust_menu_choice == 2:
                    customer = create_customer()
                    customers.append(customer)

                elif cust_menu_choice == 3:
                    customer = int(input("Enter customer number: "))
                    print("1. First name")
                    print("2. Last name")
                    print("3. Address")
                    print("4. Ph(Mobile)")
                    print("5. Ph(Work)")
                    print("6. Ph(Home)")
                    print("7. Fax(Home)")
                    print("8. Fax(Work)")
                    print("9. Email")
                    print("10. House/Land budget")
                    print("11. House only budget")
                    print("12. Is selling existing(Y/N)")
                    print("13. Land details")
                    print("14. Notes")
                    edit_choice = int(input("Enter detail to edit: "))
                    new_detail = input("Enter new details: ")
                    if new_detail.upper() == "Y":
                        new_detail = True
                    if new_detail.upper() == "N":
                        new_detail = False
                    update_details(edit_choice, new_detail, customer, customers)

                elif cust_menu_choice == 4:
                    try:
                        customer = int(input("Enter customer number to remove: "))
                        del customers[customer - 1]
                    except IndexError:
                        print("Invalid customer number.")
                    except ValueError:
                        print("Enter a valid number.")
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
    print("__________CUSTOMER MENU__________")
    print("1. Customer Details")
    print("2. Add new customer")
    print("3. Edit customer details")
    print("4. Remove customer")
    print("5. Return to main menu")


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


def list_customers(customers):
    if len(customers) == 0:
        print("No customers currently stored.")
        return
    else:
        customer_counter = 1
        print("_____________________________")
        for customer in customers:
            print("{}. {} {}".format(customer_counter, customer.fname, customer.lname))
            customer_counter += 1


def update_details(choice, details, customer, customers):
    try:

        if choice == 1:
            customers[customer - 1].edit_fname(details)

        elif choice == 2:
            customers[customer - 1].edit_lname(details)

        elif choice == 3:
            customers[customer - 1].edit_address(details)

        elif choice == 4:
            customers[customer - 1].edit_mobile_phone(details)

        elif choice == 5:
            customers[customer - 1].edit_work_phone(details)

        elif choice == 6:
            customers[customer - 1].edit_home_phone(details)

        elif choice == 7:
            customers[customer - 1].edit_home_fax(details)

        elif choice == 8:
            customers[customer - 1].edit_work_fax(details)

        elif choice == 9:
            customers[customer - 1].edit_email(details)

        elif choice == 10:
            customers[customer - 1].edit_house_land_budget(details)

        elif choice == 11:
            customers[customer - 1].edit_house_only_budget(details)

        elif choice == 12:
            customers[customer - 1].edit_is_selling_something(details)

        elif choice == 13:
            customers[customer - 1].edit_land_details(details)

        elif choice == 14:
            customers[customer - 1].edit_notes(details)
    except IndexError:
        print("Invalid customer number")
    except ValueError:
        print("Enter a valid number.")

main()

