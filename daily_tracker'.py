class Daily_tracker():
    """Formulate and store the count for the day."""

    def init(self, current_day = "", customer_count = 0, entry_times = []):

        self.current_day = current_day
        self.customer_count = customer_count
        self.entry_times = entry_times

    def __str__(self):

        return "{}, {} customers, {}".format(self.current_day, self.customer_count, self.entry_times)


