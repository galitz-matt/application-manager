import json
from application import Application


def open_data(file_path):
	with open(file_path, "r") as json_file:
		return json.load(json_file)


class JSONBuilder:

	def __init__(self, file_path):
		self._file_path = file_path
		self._data = open_data(file_path)

	def add_application(self, application: Application):
		self._data.append(application.get_attribute_map_for_json())
		self.__create_json()

	def __create_json(self):
		with open(self._file_path, "w") as json_file:
			json.dump(self._data, json_file, indent=4)
