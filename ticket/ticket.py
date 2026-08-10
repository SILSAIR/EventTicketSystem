class Ticket:
    def __init__(self, ticket_id, event_name, seat_number, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.seat_number = seat_number
        self.price = price
        self.ticket_type = "Regular"

    def reserve(self):
        if self.status == "available":
            self.status = "reserved"
            return True
        else:
            return False

    def cancel(self):
        self.status = "available"

    def display_info(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: ${self.price:.2f}")
        print(f"Status: {self.status}")

