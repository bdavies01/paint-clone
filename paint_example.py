import tkinter

# TOOLS
LINE, RECTANGLE, DRAW, OVAL, ERASE = list(range(5))
color = (0, 0, 0)

def draw_point(event):
        x = event.x
        y = event.y
        canvas.create_rectangle(x, y, x+1, y+1)
class Paint:
    def __init__(self, canvas):
        self.canvas = canvas
        self.tool, self.obj = None, None
        self.lastx, self.lasty = None, None
        self.canvas.bind('<Button-1>', self.update_xy)
        self.canvas.bind('<B1-Motion>', self.draw)

    def draw(self, event):
        if self.tool is None or self.obj is None:
            return

        x, y = self.lastx, self.lasty
        if self.tool in (LINE, RECTANGLE, DRAW, OVAL, ERASE):
            self.canvas.coords(self.obj, (x, y, event.x, event.y))

    def update_xy(self, event):
        global erasing #why is this necessary lol
        if self.tool is None:
            return
        x, y = event.x, event.y

        if self.tool == LINE: #i want switch statements
            canvas.unbind('<B1-Motion>')
            canvas.bind('<B1-Motion>', self.draw)
            self.obj = self.canvas.create_line((x, y, x, y))

        elif self.tool == RECTANGLE:
            canvas.unbind('<B1-Motion>')
            canvas.bind('<B1-Motion>', self.draw)
            self.obj = self.canvas.create_rectangle((x, y, x, y))

        elif self.tool == DRAW:
            erasing = 0
            self.obj = None
            canvas.unbind('<B1-Motion>')
            canvas.bind('<B1-Motion>', self.draw_point)

        elif self.tool == ERASE:
            erasing = 1
            self.obj = None
            canvas.unbind('<B1-Motion>')
            canvas.bind('<B1-Motion>', self.draw_point)

        elif self.tool == OVAL:
            canvas.unbind('<B1-Motion>')
            canvas.bind('<B1-Motion>', self.draw)
            self.obj = self.canvas.create_oval((x, y, x, y))

        self.lastx, self.lasty = x, y

    def draw_point(self, event):
        x = event.x
        y = event.y
        if erasing == 1:
            canvas.create_rectangle((x, y, x+4, y+4), fill = 'white', outline = 'white')

        elif erasing == 0:
            canvas.create_rectangle((x, y, x+1, y+1))

    def selecttool(self, tool):
        if tool == 0: #no switch statements in python lol nice
            print("Line tool selected")
        elif tool == 1:
            print("Rectangle tool selected")
        elif tool == 2:
            print("Free draw tool selected")
        elif tool == 3:
            print("Oval tool selected")
        elif tool == 4:
            print("Erase tool selected")
        self.tool = tool

class Tool:
    def __init__(self, whiteboard, parent=None):
        self.whiteboard = whiteboard

        frame = tkinter.Frame(parent)
        self.currtool = None

        for i, (text, t) in enumerate((('L', LINE), ('R', RECTANGLE), ('O', OVAL), ('D', DRAW), ('E', ERASE))):
            lbl = tkinter.Label(frame, text=text, width=2, relief='raised')
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


root = tkinter.Tk()
root.wm_title("Paint")
canvas = tkinter.Canvas(highlightbackground='black')
canvas.configure(background = 'white', width = 640, height = 480)
whiteboard = Paint(canvas)
tool = Tool(whiteboard)
canvas.pack(fill='both', expand=True, padx=6, pady=6)

root.mainloop()