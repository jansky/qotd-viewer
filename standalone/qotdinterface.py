#!/usr/bin/python
#    Quote Of The Day Viewer
#    Copyright (C) 2013  Ian Duncan
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from Tkinter import *
import socket
import sys

class qotdApp:

	def aboutWindow(self):
	
		#About Dialog
		about = Toplevel()
		

		self.titleLabel = Label(about, text="QOTD Viewer",font=("sans-serif", 20))
		self.titleLabel.grid(row=0, column=0)

		self.versionLabel = Label(about, text="Version 1",font=("sans-serif",14))
		self.versionLabel.grid(row=0,column=1)

		self.authorLabel = Label(about, text="By Ian Duncan")
		self.authorLabel.grid(row=1)

		self.gplLabel = Message(about,text="This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public Licensealong with this program.  If not, see <http://www.gnu.org/licenses/>.",width=600)
		self.gplLabel.grid(row=1,column=1)

		
	
	def __init__(self, master):

			
		frame = Frame(master)
		frame.pack()

		self.prompt = Label(frame, text="Server Address: ")
		self.prompt.grid(row=0, column=0, sticky=W)

		self.sAEntry = Entry(frame)
		self.sAEntry.grid(row=0, column=1, sticky=W)

		self.go = Button(frame, text="View QOTD", command=self.getQuote)
		self.go.grid(row=0, column=2, sticky=W)

		self.aboutButton = Button(frame, text="About", command=self.aboutWindow)
		self.aboutButton.grid(row=0,column=3,sticky=W)

		self.viewQuote = Text(frame, height=10, width=100)
		self.viewQuote.grid(row=1, columnspan=4)
		

		frame.columnconfigure(2, weight=4)

	def getQuote(self):

		self.viewQuote.config(state=NORMAL)
		
		self.viewQuote.delete(1.0, END)
		
		try:
			
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		except socket.error:

			print 'OOPS! Error Creating Socket. Could Not Get QOTD'
			return None

		host = self.sAEntry.get()
		port = 17

		try:

			remote_ip = socket.gethostbyname(host)

		except socket.gaierror:

			print 'OOPS! Unable To Resolve Hostname. Could Not Get QOTD'
			return None

		s.connect((remote_ip, port))

		try:

			qotd = s.recv(4096)

			self.viewQuote.insert(INSERT, qotd)

		except socket.error:

			print 'OOPS! Unable To Receive Message. Could Not Get QOTD'
			return None

		self.viewQuote.config(state=DISABLED)
			
		
		


root = Tk(className='quote of the day viewer')
app = qotdApp(root)

root.mainloop()
	
		

