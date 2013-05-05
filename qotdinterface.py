from Tkinter import *

class qotdApp:
	
	def __init__(self, master):
	
		frame = Frame(master)
		frame.pack()

		self.prompt = Label(frame, text="Server Address: ")
		self.prompt.grid(row=0, column=0, sticky=W)

		self.sAEntry = Entry(frame)
		self.sAEntry.grid(row=0, column=1, sticky=W)

		self.go = Button(frame, text="View QOTD", command=self.reportAddress)
		self.go.grid(row=0, column=2, sticky=W)

		self.viewQuote = Text(frame, height=5)
		self.viewQuote.grid(row=1, columnspan=3)

		frame.columnconfigure(2, weight=4)

	def reportAddress(self):
		
		print self.sAEntry.get()


root = Tk(className='quote of the day viewer')
app = qotdApp(root)

root.mainloop()
	
		

