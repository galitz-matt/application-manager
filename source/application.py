from datetime import time


class Application:

	def __init__(self, company, position, date, status):
		self._company: str = company
		self._position: str = position
		self._date: time = date
		self._status: status = status

	def get_company(self):
		return self._company

	def get_position(self):
		return self._position

	def get_data(self):
		return self._date

	def get_status(self):
		return self._status

	def set_status(self, new_status):
		self._status = new_status