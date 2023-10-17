from datetime import time

class Application:

	def __init__(self, company, position, date, status):
		self._company: str = company
		self._position: str = position
		self._date: time = date
		self._status: