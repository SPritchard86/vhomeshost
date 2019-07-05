"""
Program to count people viewing a property, send reports to consultant and capture potential customer details.
Author: Stephen Pritchard
Date: 1/07/2019
"""

from customer import Customer
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from daily_tracker import Dailytracker
import datetime
import smtplib

REPORT_DAYS = ["Sunday", "Tuesday"]
CONSULTANT_EMAILS = ["stephen.pritchard@my.jcu.edu.au"]
CONSULTANT_NAME = ["Stephen"]
CURRENT_WEEK_FILE = "customers.csv"
MY_ADDRESS = 'valuehomeshost@gmail.com'
PASSWORD = 'Value2019'
HOST_NAME = "Steve Pritchard"
LOCATION = "Elliot Springs"
CUSTOMER_TEMPLATE = """Dear {CONSULTANT},

A customer would like for you to contact them in relation to answering enquiries about a project in {LOCATION}.
Their details follow.

               First name: {FIRST_NAME}
                Last name: {LAST_NAME}
                    Email: {EMAIL}
                  Address: {ADDRESS}
              Work number: {WORK_NUMBER}
              Home number: {HOME_NUMBER}
            Mobile number: {MOBILE_NUMBER}
                 Work fax: {WORK_FAX}
                 Home fax: {HOME_FAX}
        House/Land budget: {HOUSE_LAND_BUDGET}
        House only budget: {HOUSE_ONLY_BUDGET}
Selling existing property: {SELLING_EXISTING}
             Land details: {LAND_DETAILS}
                    Notes: {NOTES}


{FURTHER_INFO}

Yours Truly,
{HOST_NAME}"""

REPORT_TEMPLATE_1 = """Dear {CONSULTANT},

Following is a summary of the last 7 days of customer activity at the open home in {LOCATION}.

"""

REPORT_TEMPLATE_2 = """{DAY} {DATE}:
Customers just looking: {CASUAL_CUSTOMERS}
Customers potentially building: {BUILD_CUSTOMERS}
Entry times: {TIMES}
__________________________________________________
"""

REPORT_TEMPLATE_3 = """

Yours Truly,
{HOST_NAME}"""


def main():
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    casual_customer_count = 0
    build_customer_count = 0
    view_times = []
    customers = []
    current_datetime = datetime.datetime.now()
    today = current_datetime.strftime("%A")
    todays_date = current_datetime.strftime("%x")

    print("--- Host Companion App ---")
    print_menu(casual_customer_count, build_customer_count, today)
    menu_choice = int(input(">>> "))

    while menu_choice != 8:
        if menu_choice == 1:
            casual_customer_count += 1
            view_times.append(get_current_time())
            pass
        elif menu_choice == 2:
            build_customer_count += 1
            view_times.append(get_current_time())
        elif menu_choice == 3:
            print("Entry times for todays customers: ")
            print(view_times)
        elif menu_choice == 4:
            list_customers(customers)
            print_customer_menu()
            cust_menu_choice = int(input(">>> "))
            while cust_menu_choice != 6:
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
                elif cust_menu_choice == 5:
                    customer = int(input("Enter customer number to forward via email: "))
                    further_info = input("Please enter any additional customer information: ")
                    msg = MIMEMultipart()  # create a message
                    msg['From'] = MY_ADDRESS
                    msg['To'] = CONSULTANT_EMAILS[0]
                    msg['Subject'] = "Customer Details, location: " + LOCATION
                    msg.attach(MIMEText(CUSTOMER_TEMPLATE.format(CONSULTANT=CONSULTANT_NAME[0], LOCATION=LOCATION,
                                                                 FIRST_NAME=customers[customer - 1].fname,
                                                                 LAST_NAME=customers[customer - 1].lname,
                                                                 EMAIL=customers[customer - 1].email,
                                                                 ADDRESS=customers[customer - 1].address,
                                                                 WORK_NUMBER=customers[customer - 1].work_phone,
                                                                 HOME_NUMBER=customers[customer - 1].home_phone,
                                                                 MOBILE_NUMBER=customers[customer - 1].mobile_phone,
                                                                 WORK_FAX=customers[customer - 1].work_fax,
                                                                 HOME_FAX=customers[customer - 1].home_fax,
                                                                 HOUSE_LAND_BUDGET=customers[customer - 1]
                                                                 .house_land_budget,
                                                                 HOUSE_ONLY_BUDGET=customers[customer - 1]
                                                                 .house_only_budget,
                                                                 SELLING_EXISTING=customers[customer - 1]
                                                                 .is_selling_existing,
                                                                 LAND_DETAILS=customers[customer - 1].land_details,
                                                                 NOTES=customers[customer - 1].notes,
                                                                 FURTHER_INFO=further_info,
                                                                 HOST_NAME=HOST_NAME), 'plain'))
                    s.send_message(msg)
                    print("Email sent.")
                    del msg

                else:
                    print("Invalid option")
                print_customer_menu()
                cust_menu_choice = int(input(">>> "))

        elif menu_choice == 5:
            in_file = open("daily_tracker.csv", "r")
            daily_backup = in_file.read()
            split_backup = daily_backup.split(",")
            print("Loading last saved details for {}.".format(split_backup[0]))
            print("Casual customers: {}".format(split_backup[2]))
            print("Potential build customers: {}".format(split_backup[3]))
            print("Customer entry times: {}".format([time + ", " for time in split_backup[4:]]))
            in_file.close()

            casual_customer_count = int(split_backup[2])
            build_customer_count = int(split_backup[3])
            for time in split_backup[4:]:
                view_times.append(time)

        elif menu_choice == 6:
            if not view_times:
                view_times = ['None']
            final_count = Dailytracker(today, todays_date, str(casual_customer_count), str(build_customer_count),
                                       view_times)
            final_count_string = final_count.current_day + "," + final_count.current_date + "," + \
                                 final_count.casual_customer_count + "," + final_count.build_customer_count
            for time in final_count.entry_times:
                final_count_string += "," + str(time)

            print("Saving final day count...")
            out_file = open("entry_history.csv", 'a+')
            out_file.write(final_count_string)
            out_file.write("\n")
            out_file.close()
            print("Saved in entry_history.csv")
            print("Goodbye")

        elif menu_choice == 7:
            confirm_report = input("This will send the last 7 days of information to your nominated consultant."
                                   " Continue? (Y/N) ").upper()
            if confirm_report == "Y":
                template_7days_1 = REPORT_TEMPLATE_1.format(CONSULTANT=CONSULTANT_NAME[0], LOCATION=LOCATION)

                template_7days_2 = ""
                last_7_days = get_last_7_days("entry_history.csv")
                for day in reversed(last_7_days):
                    template_7days_2 += REPORT_TEMPLATE_2.format(DAY=day[0], DATE=day[1], CASUAL_CUSTOMERS=day[2],
                                                                 BUILD_CUSTOMERS=day[3],
                                                                 TIMES=[time for time in day[4:]])
                    print(template_7days_2)
                template_7days_3 = REPORT_TEMPLATE_3.format(HOST_NAME=HOST_NAME)
                total_template = template_7days_1 + template_7days_2 + template_7days_3
                print(total_template)
                msg = MIMEMultipart()  # create a message
                msg['From'] = MY_ADDRESS
                msg['To'] = CONSULTANT_EMAILS[0]
                msg['Subject'] = "Weekly report, location: " + LOCATION
                msg.attach(MIMEText(template_7days_1 + template_7days_2 + template_7days_3))
                s.send_message(msg)
                print("Email sent.")
                del msg

        else:
            print("Invalid input")
        print_menu(casual_customer_count, build_customer_count, today)
        menu_choice = int(input(">>> "))

    todays_count = Dailytracker(today, todays_date, str(casual_customer_count), str(build_customer_count), view_times)
    today_string = todays_count.current_day + "," + todays_count.current_date + ","\
                   + todays_count.casual_customer_count + "," + todays_count.build_customer_count
    for time in todays_count.entry_times:
        today_string += "," + str(time)
    print("Saving current daily count...")
    out_file = open("daily_tracker.csv", 'w')
    out_file.write(today_string)
    out_file.close()
    print("Saved in daily_tracker.csv")
    print("Goodbye")


def print_menu(casual_count, build_count, today):
    """Prints the main menu for customer counter"""
    print("Today is {}".format(today))
    if today in REPORT_DAYS:
        print("Today is a reporting day. Make sure to report after 3:30pm!")
    print("Current casual customer count: {}".format(casual_count))
    print("Current potential 6-12 months build customer count: {}".format(build_count))
    print("________________MENU________________")
    print("1. Count casual customer")
    print("2. Count potential build customer")
    print("3. View entry times")
    print("4. Customer details")
    print("5. reload backup daily details (Use in case of accidental quit)")
    print("6. End of day save ")
    print("7. Send weekly report")
    print("8. Exit")


def print_customer_menu():
    print("__________CUSTOMER MENU__________")
    print("1. Customer Details")
    print("2. Add new customer")
    print("3. Edit customer details")
    print("4. Remove customer")
    print("5. Forward customer details via email")
    print("6. Return to main menu")


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
    return Customer(fname, lname, address, mobile_phone, work_phone, home_phone, home_fax, work_fax, email,
                    house_land_budget, house_only_budget, is_selling_existing, land_details, notes)


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


def get_last_7_days(history):
    last_7_lines = []
    in_file = open(history, "r")
    line_list = in_file.readlines()
    in_file.close()
    for line in line_list[-1:-8:-1]:
        line = line.strip('\n')
        line = line.split(',')
        last_7_lines.append(line)
    return last_7_lines


main()
