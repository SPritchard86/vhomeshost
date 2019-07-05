class Dailytracker():
    """Formulate and store the count for the day."""

    def __init__(self, current_day = "", current_date = "", casual_customer_count = 0, build_customer_count = 0, entry_times = []):

        self.current_day = current_day
        self.current_date = current_date
        self.casual_customer_count = casual_customer_count
        self.build_customer_count = build_customer_count
        self.entry_times = entry_times

    def __str__(self):

        return "{}, {} customers, {}".format(self.current_day, self.customer_count, self.entry_times)


