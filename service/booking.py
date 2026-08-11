from service.factory import TicketFactory
from service.payment import Payment
from service.notification import Notification

class Booking:
    def __init__(self, payment=None, notification=None):
        self.payment = payment or Payment()
        self.notification = notification or Notification()

    def book_ticket(self, event, ticket_type, ticket_id, seat_number, price, **kwargs):
        if event.is_sold_out():
            raise ValueError("Cannot book, event is sold out")

        ticket = TicketFactory.create_ticket(ticket_type, ticket_id, event.name, seat_number, price, **kwargs)

        total_price = event.calculate_price(ticket)
        self.payment.process(total_price)

        event._book_seat()
        ticket.reserve()

        self.notification.send(f"Ticket {ticket.ticket_id} booked for {event.name}")

        return ticket
