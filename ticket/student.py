from .ticket import Ticket

class StudentTicket(Ticket):
    def __init__(self, ticket_id, event_name, seat_number, price, student_id):
        super().__init__(ticket_id, event_name, seat_number, price)
        self.student_id = student_id
        self.ticket_type = "Student"