import tkinter as tk


class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tkinter GUI")

        self.add_app_button = None
        self.application_frame = None
        self.company_entry = None
        self.position_entry = None
        self.date_entry = None
        self.status_entry = None
        self.go_back_button = None

        self.initialize_ui()

    def initialize_ui(self):
        self.create_home_page()
        self.create_application_form()

    def create_home_page(self):
        self.add_app_button = tk.Button(self.root, text="Add Application", command=self.show_application_form)
        self.add_app_button.pack()

    def create_application_form(self):
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

        self.go_back_button = tk.Button(self.application_frame, text="Go Back", command=self.hide_application_form)
        self.go_back_button.pack()

    def show_application_form(self):
        self.add_app_button.pack_forget()
        self.application_frame.pack()

    def hide_application_form(self):
        self.application_frame.pack_forget()
        self.add_app_button.pack()

    def run(self):
        self.root.mainloop()