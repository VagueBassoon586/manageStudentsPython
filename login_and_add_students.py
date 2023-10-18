import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.geometry('800x750+360+25')
		self.title('Manage Students')
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}
		for F in (PageOne, PageTwo):
			page_name = F.__name__
			frame = F(parent = container, controller = self)
			self.frames[page_name] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")

		self.show_frame("PageOne")

	def show_frame(self, page_name):
		"""

		:param page_name:
		"""
		frame = self.frames[page_name]
		frame.tkraise()


class PageOne(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.login_sign = tk.Label(self, text = 'LOGIN', fg = 'black', font = ('Arial', 30))
		self.login_sign.place(x = 220, y = 270)

		self.user = tk.Label(self, text = 'User Name: ', fg = 'black', font = ('Arial', 10))
		self.user.place(x = 220, y = 330)

		self.user_entry = tk.Entry(self, width = 45)
		self.user_entry.place(x = 300, y = 332)

		self.passw = tk.Label(self, text = 'Password: ', fg = 'black', font = ('Arial', 10))
		self.passw.place(x = 220, y = 370)

		self.passw_entry = tk.Entry(self, show = '•', width = 45)
		self.passw_entry.place(x = 300, y = 372)

		self.login = tk.Button(self, text = 'Log in', bg = 'gray', command = self.login)
		self.login.place(x = 300, y = 400)

		self.clear = tk.Button(self, text = 'Clear', bg = 'gray', command = self.clear)
		self.clear.place(x = 350, y = 400)

	def login(self):
		login_file = open('C:\\Users\\Administrator\\Desktop\\File\\Python\\Tkinter\\Manage_students\\Login_and_add_students_pycode\\login.txt', 'r')
		user = list(login_file)
		login_file.close()
		user[0] = user[0].replace('\n', '')
		name = str(self.user_entry.get())
		password = str(self.passw_entry.get())
		check = [name, password]
		del name, password
		if check == user:
			self.controller.show_frame("PageTwo")

	def clear(self):
		self.user_entry.delete(0, 'end')
		self.passw_entry.delete(0, 'end')


class PageTwo(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.tree = self.create_tree_widget()

	def create_tree_widget(self):
		columns = ('name', 'class', 'birth_place', 'scores')
		self.tree = ttk.Treeview(self, columns = columns, show = 'headings')

		self.tree.heading('name', text = 'Name')
		self.tree.heading('class', text = 'Class')
		self.tree.heading('birth_place', text = 'Hometown')
		self.tree.heading('scores', text = 'Score')
		self.tree.pack(side = 'top', fill = 'both')
		self.add = tk.Button(self, height = '1', width = '3', text = '+', fg = 'green', bg = 'gray', font = ('Helvetica', 18, 'bold'), command = self.insert_entry)
		self.add.pack(anchor = "w", side = "bottom")

		students_data = open("C:\\Users\\Administrator\\Desktop\\File\\Python\\Tkinter\\Manage_students\\Login_and_add_students_pycode\\students_data.txt", "r", encoding = "utf8")
		data = list(students_data)
		students_data.close()
		if len(data) > 0:
			for i in range(len(data)):
				datum = data[i].split("| ")
				datum[3] = datum[3].replace('\n', '')
				ten, lop, que, diem = datum[0], datum[1], datum[2], datum[3]
				self.tree.insert('', tk.END, values = (ten, lop, que, diem))
			del data, datum, ten, lop, que, diem

		return self.tree

	def insert_entry(self):
		self.name_lbl = tk.Label(self, text = 'Name:')
		self.name_lbl.place(x = 180, y = 580)
		self.name = tk.Entry(self, width = 40)
		self.name.place(x = 260, y = 580)

		self.class_lbl = tk.Label(self, text = 'Class:')
		self.class_lbl.place(x = 180, y = 610)
		self.class_ = tk.Entry(self, width = 40)
		self.class_.place(x = 260, y = 610)

		self.birth_place_lbl = tk.Label(self, text = 'Hometown:')
		self.birth_place_lbl.place(x = 180, y = 640)
		self.birth_place = tk.Entry(self, width = 40)
		self.birth_place.place(x = 260, y = 640)

		self.scores_lbl = tk.Label(self, text = 'Score:')
		self.scores_lbl.place(x = 180, y = 670)
		self.scores = tk.Entry(self, width = 40)
		self.scores.place(x = 260, y = 670)

		self.enter = tk.Button(self, text = 'Add', bg = 'gray', command = self.insert)
		self.enter.place(x = 260, y = 700)

		self.clear = tk.Button(self, text = 'Clear', bg = 'gray', command = self.clear)
		self.clear.place(x = 300, y = 700)

		self.done = tk.Button(self, text = 'Done', bg = 'gray', command = self.done)
		self.done.place(x = 345, y = 700)

	def insert(self):
		ten = str(self.name.get())
		lop = str(self.class_.get())
		que = str(self.birth_place.get())
		diem = str(self.scores.get())
		self.tree.insert('', tk.END, values = (ten, lop, que, diem))
		data = open("C:\\Users\\Administrator\\Desktop\\File\\Python\\Tkinter\\Manage_students\\Login_and_add_students_pycode\\students_data.txt", "a+", encoding = "utf8")
		infor = f"{ten} | {lop} | {que} | {diem} \n"
		data.write(infor)
		data.close()
		del ten, lop, que, diem
		self.name.delete(0, 'end')
		self.class_.delete(0, 'end')
		self.birth_place.delete(0, 'end')
		self.scores.delete(0, 'end')

	def clear(self):
		self.name.delete(0, 'end')
		self.class_.delete(0, 'end')
		self.birth_place.delete(0, 'end')
		self.scores.delete(0, 'end')

	def done(self):
		self.name_lbl.destroy()
		self.name.destroy()
		self.class_lbl.destroy()
		self.class_.destroy()
		self.birth_place_lbl.destroy()
		self.birth_place.destroy()
		self.scores_lbl.destroy()
		self.scores.destroy()
		self.enter.destroy()
		self.clear.destroy()
		self.done.destroy()


if __name__ == '__main__':
	app = App()
	app.mainloop()
