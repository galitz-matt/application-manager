import tkinter as tk


class GUI:

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("My Application Manager")


if __name__ == "__main__":
	app = GUI()
	app.root.mainloop()