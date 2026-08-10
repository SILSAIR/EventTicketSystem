from event.event import event

class Workshop(event):
    def __init__(self, name, date, location, capacity, instructor):
        super().__init__(name, date, location, capacity)
        self.instructor = instructor

    def calculate_price(self, ticket_type):
        return ticket_type.price

    def get_details(self):
        return f"Workshop: {self.name} with {self.instructor} on {self.date} at {self.location}"