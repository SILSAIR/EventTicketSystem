from abc import ABC, abstractmethod
#this class the blueprint for the other events
class event(ABC):
	def __init__(self, name, date, location, capacity):
		self.name = name
		self.date = date
		self.location = location
		self.capacity = capacity
		self.booked_seats = 0
		raise ValueError() if self.capacity <= 0 else None
	
	
	
	#abstract function to calculate the price based on the ticket_type.price
	# (I hope its ticket_type = ticket* (number based on how expansive it is))
	@abstractmethod
	def calculate_price(self, ticket_type):
		pass
	
	#return string of details
	@abstractmethod
	def get_details(self):
		pass
	#set of function can be helpful
	#first is the event full?
	def is_sold_out(self):
		return self.booked_seats >= self.capacity
	#how many left in the event
	def available_seats(self):
		return self.capacity - self.booked_seats
	#this function is protected If need to be deleted
	def _book_seat(self):
		if self.is_sold_out():
			raise ValueError("Event is sold out")
		self.booked_seats += 1
	