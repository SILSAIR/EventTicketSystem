from event.event import event

class Sport(event):
    def __init__(self, name, date, location, capacity, teams , capten):
        super().__init__(name, date, location, capacity)
        self.captens = capten
        self.teams = teams

    def calculate_price(self, ticket_type):
        return ticket_type.price

    def get_details(self):
        return f"Sport: {self.name} ({self.teams}) on {self.date} at {self.location}"