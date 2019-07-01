"""
Program to count people viewing a property.

"""


import datetime

REPORT_DAYS = ["Sunday", "Tuesday"]


def main():

    current_datetime = datetime.datetime.now()
    print("--- Customer Counter ---")
    print("Today is {}".format(current_datetime.strftime("%A")))

    if current_datetime.strftime("%A") in REPORT_DAYS:
        print("Today is a reporting day. Make sure to report after 3:30pm!")


main()

