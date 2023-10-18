import tkinter as tk
from json_builder import JSONBuilder
from application import Application

json_builder = JSONBuilder("../resources/applications.json")


class GUI:

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Tkinter GUI")
		self.__initialize_ui()

	def __initialize_ui(self):
		self.__initialize_variables()
		self.__create_home_page()
		self.__create_application_form()

	def __create_home_page(self):
		self.add_app_button = tk.Button(self.root, text="Add Application", command=self.__show_application_form)
		self.add_app_button.pack()

	def __create_application_form(self):
		self.application_frame = tk.Frame(self.root)
		self.application_frame.pack_forget()

		tk.Label(self.application_frame, text="Company:").pack()
		self.company_entry = tk.Entry(self.application_frame)
		self.company_entry.pack()

		tk.Label(self.application_frame, text="Position:").pack()
		self.position_entry = tk.Entry(self.application_frame)
		self.position_entry.pack()

		tk.Label(self.application_frame, text="Date:").pack()
		self.date_entry = tk.Entry(self.application_frame)
		self.date_entry.pack()

		tk.Label(self.application_frame, text="Status:").pack()
		self.status_entry = tk.Entry(self.application_frame)
		self.status_entry.pack()

		self.go_back_button = tk.Button(self.application_frame, text="Go Back", command=self.__hide_application_form)
		self.go_back_button.pack()

		self.enter_button = tk.Button(self.application_frame, text="Enter", command=self.__submit_application)
		self.enter_button.pack()

	def __initialize_variables(self):
		self.add_app_button = None
		self.application_frame = None
		self.company_entry = None
		self.position_entry = None
		self.date_entry = None
		self.status_entry = None
		self.go_back_button = None

	def __show_application_form(self):
		self.add_app_button.pack_forget()
		self.application_frame.pack()

	def __hide_application_form(self):
		self.application_frame.pack_forget()
		self.add_app_button.pack()

	def __submit_application(self):
		global json_builder
		company = self.company_entry.get()
		position = self.position_entry.get()
		date = self.date_entry.get()
		status = self.status_entry.get()
		application_data = {
			"Company": company,
			"Position": position,
			"Date": date,
			"Status": status
		}
		json_builder.add_application(application_data)

	def run(self):
		self.root.mainloop()


if __name__ == "__main__":
	gui = GUI()
	gui.run()
