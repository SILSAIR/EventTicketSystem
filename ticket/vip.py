from .ticket import Ticket

class VIPTicket(Ticket):
    def __init__(self, ticket_id, event_name, seat_number, price):
        super().__init__(ticket_id, event_name, seat_number, price)
        self.ticket_type = "VIP"