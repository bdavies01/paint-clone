import Tkinter as tk
from PIL import ImageTk as im
DRAW, ERASE, RECTANGLE, OVAL, LINE = list(range(5))
RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, DEFAULT = list(range(7))

class Paint:
	def __init__(self, canvas):
		self.canvas = canvas
		self.startX = self.startY = None
		self.oldX = self.oldY = None
		self.x = self.y = 0
		self.rect = self.oval = self.line = None
		self.tool = None
		self.color = "black"
		self.b1 = None
		self.canvas.bind("<ButtonPress-1>", self.on_button_press)
		self.canvas.bind("<Motion>", self.on_move_press)
		self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

	def on_button_press(self, event):
		self.startX = self.canvas.canvasx(event.x)
		self.startY = self.canvas.canvasy(event.y)
		self.b1 = "down"

		if not self.rect:
			self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline = self.color)

		if not self.oval:
			self.oval = self.canvas.create_oval(self.x, self.y, 1, 1, outline = self.color)

		if not self.line:
			self.line = self.canvas.create_line(self.y, self.y, 1, 1, fill = self.color)

	def on_move_press(self, event):
		if self.b1 == "down":
			curX = self.canvas.canvasx(event.x)
			curY = self.canvas.canvasy(event.y)

			if self.tool == DRAW:

				if self.oldX is not None and self.oldY is not None:

					self.canvas.create_line(self.oldX, self.oldY, curX, curY, fill = self.color)

				self.oldX = curX
				self.oldY = curY

			elif self.tool == ERASE:

				if self.oldX is not None and self.oldY is not None:
					self.canvas.create_rectangle(self.oldX, self.oldY, curX + 5, curY + 5, fill = 'white', outline = 'white')
					
				self.oldX = curX
				self.oldY = curY

			elif self.tool == RECTANGLE:
				self.canvas.coords(self.rect, self.startX, self.startY, curX, curY)

			elif self.tool == OVAL:
				self.canvas.coords(self.oval, self.startX, self.startY, curX, curY)

			elif self.tool == LINE:
				self.canvas.coords(self.line, self.startX, self.startY, curX, curY)

	def on_button_release(self, event):
		self.b1 = "up"
		self.oldX = None
		self.oldY = None
		self.rect = None
		self.oval = None
		self.line = None

	def selecttool(self, tool):
		self.tool = tool

	def changecolor(self, color):
		if color == 0:
			self.color = "red"

		elif color == 1:
			self.color = "orange"

		elif color == 2:
			self.color = "yellow"

		elif color == 3:
			self.color = "green"

		elif color == 4:
			self.color = "blue"

		elif color == 5:
			self.color = "purple"

		elif color == 6:
			self.color = "black"

class Tool:
	def __init__(self, whiteboard, parent = None):
		self.whiteboard = whiteboard
		frame = tk.Frame(parent)
		self.currtool = None
		toollabel = tk.Label(frame, text = "Tools", width = 3)
		toollabel.pack(padx=6)
		frame.pack(side = 'left', fill = 'y', expand = True, pady = 6)

		for i, (text, t) in enumerate((('L', LINE), ('R', RECTANGLE), ('O', OVAL), ('D', DRAW), ('E', ERASE))):
			lbl = tk.Label(frame, text=text, width=2, relief='raised')
			lbl.tool = t
			lbl.bind('<Button-1>', self.updatetool)
			lbl.pack(padx=6, pady=6*(i % 2))

		frame.pack(side='left', fill='y', expand=True, pady=6)

	def updatetool(self, event):
		lbl = event.widget

		if self.currtool:
			self.currtool['relief'] = 'raised'

		lbl['relief'] = 'sunken'
		self.currtool = lbl
		self.whiteboard.selecttool(lbl.tool)

class Color:
	def __init__(self, whiteboard, parent = None):
		redimg = im.PhotoImage(file = "C:\\Users\\Bert\\Documents\\GitHub\\paint-program\\colors\\red.png")
		orangeimg = im.PhotoImage(file = "C:\\Users\\Bert\\Documents\\GitHub\\paint-program\\colors\\orange.png")
		yellowimg = im.PhotoImage(file = "C:\\Users\\Bert\\Documents\\GitHub\\paint-program\\colors\\yellow.png")
		greenimg = im.PhotoImage(file = "C:\\Users\\Bert\\Documents\\GitHub\\paint-program\\colors\\green.png")
		blueimg = im.PhotoImage(file = "C:\\Users\\Bert\\Documents\\GitHub\\paint-program\\colors\\blue.png")
		purpleimg = im.PhotoImage(file = "C:\\Users\\Bert\\Documents\\GitHub\\paint-program\\colors\\purple.png")
		defaultimg = im.PhotoImage(file = "C:\\Users\\Bert\\Documents\\Github\\paint-program\\colors\\black.png")
		self.whiteboard = whiteboard
		frame = tk.Frame(parent)
		self.currcolor = None
		colorlabel = tk.Label(frame, text = "Colors", width = 4)
		colorlabel.pack(padx = 6)
		frame.pack(side = 'right', fill = 'y', expand = True, pady = 6)

		for i, (text, t) in enumerate((('R', RED), ('O', ORANGE), ('Y', YELLOW), ('G', GREEN), ('B', BLUE), ('P', PURPLE), ('D', DEFAULT))):
			if text == "R":
				lbl = tk.Label(frame, image = redimg, width = 16, height = 16, relief = 'raised')
				lbl.photo = redimg
				lbl.color = 0
			elif text == "O":
				lbl = tk.Label(frame, image = orangeimg, width = 16, height = 16, relief = 'raised')
				lbl.photo = orangeimg
				lbl.color = 1
			elif text == "Y":
				lbl = tk.Label(frame, image = yellowimg, width = 16, height = 16, relief = 'raised')
				lbl.photo = yellowimg
				lbl.color = 2
			elif text == "G":
				lbl = tk.Label(frame, image = greenimg, width = 16, height = 16, relief = 'raised')
				lbl.photo = greenimg
				lbl.color = 3
			elif text == "B":
				lbl = tk.Label(frame, image = blueimg, width = 16, height = 16, relief = 'raised')
				lbl.photo = blueimg
				lbl.color = 4
			elif text == "P":
				lbl = tk.Label(frame, image = purpleimg, width = 16, height = 16, relief = 'raised')
				lbl.photo = purpleimg
				lbl.color = 5
			elif text == "D":
				lbl = tk.Label(frame, image = defaultimg, width = 16, height = 16, relief = 'raised')
				lbl.photo = defaultimg
				lbl.color = 6
			lbl.bind("<Button-1>", self.updatecolor)
			lbl.pack(padx = 6, pady=6*(i % 2))

		frame.pack(side='right', fill = 'y', expand = True, pady = 6)

	def updatecolor(self, event):
		lbl = event.widget
		if self.currcolor:
			self.currcolor['relief'] = 'raised'

		lbl['relief'] = 'sunken'
		self.currcolor = lbl
		self.whiteboard.changecolor(lbl.color)

print("\nPaly Robotics Summer Camp Example Paint Program")
print("\nL: Line tool")
print("R: Rectangle tool")
print("O: Oval tool")
print("D: Free draw tool")
print("E: Erase tool")
print("\nHave fun!")

root = tk.Tk()
root.wm_title("Sample Paint Program")
root.iconbitmap(r"C:\\Users\\Bert\\Documents\\Github\\paint-program\\brush.ico")
canvas = tk.Canvas(root, highlightbackground = 'black')
canvas.configure(background = 'white', width = 640, height = 480)
whiteboard = Paint(canvas)
tool = Tool(whiteboard)
color = Color(whiteboard)
canvas.pack(fill = 'both', expand = True, padx = 6, pady = 6)
root.mainloop()