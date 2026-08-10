from event.event import event

class Concert(event):
    def __init__(self, name, date, location, capacity, artist):
        super().__init__(name, date, location, capacity)
        self.artist = artist

    def calculate_price(self, ticket_type):
        return ticket_type.price

    def get_details(self):
        return f"Concert: {self.name} by {self.artist} on {self.date} at {self.location}"