
class Application:

	def __init__(self, company, position, date, status):
		self._company: str = company
		self._position: str = position
		self._date: date = date
		self._status: status = status

	def get_company(self):
		return self._company

	def get_position(self):
		return self._position

	def get_date(self):
		return self._date

	def get_status(self):
		return self._status

	def set_company(self, company):
		self._company = company

	def set_position(self, position):
		self._position = position

	def set_date(self, date):
		self._date = date

	def set_status(self, status):
		self._status = status

	def get_attribute_map_for_json(self):
		return {
			"company": self._company,
			"position": self._position,
			"date": self._date,
			"status": self._status
		}
