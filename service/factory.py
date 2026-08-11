from ticket.regular import RegularTicket
from ticket.vip import VIPTicket
from ticket.student import StudentTicket

class TicketFactory:
   
    ticket_types = {
        "regular": RegularTicket,
        "vip": VIPTicket,
        "student": StudentTicket
    }

    @staticmethod
    def register_type(name, ticket_class):
        TicketFactory.ticket_types[name.lower()] = ticket_class

    @staticmethod
    def create_ticket(ticket_type, ticket_id, event_name, seat_number, price, **kwargs):
        ticket_class = TicketFactory.ticket_types.get(ticket_type.lower())
        if not ticket_class:
            raise ValueError(f"Unknown ticket type: {ticket_type}")
        return ticket_class(ticket_id, event_name, seat_number, price, **kwargs)
