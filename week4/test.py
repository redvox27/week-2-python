from tkinter import *
from random import randint
import time
class Test:
    root = Tk()
    def __init__(self,root):
        self.root = root
        self.canvas = Canvas(root, width=1200, height=600, bg='white')  # 0,0 is top left corner
        self.canvas.pack(expand=YES, fill=BOTH)

        self.rootButton =Button(root, text='Quit', command=root.quit).pack()

        self.canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis
        self.canvas.create_line(50, 550, 50, 50, width=2)  # y-axis


    def value_to_y(val):
        return 550 - 5 * val


    # init global vars
    s = 1
    x2 = 50
    y2 = value_to_y(randint(0, 100))

    def create_line(self):
        # x-axis
        for i in range(23):
            x = 50 + (i * 50)
            self.canvas.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.canvas.create_text(x, 550, text='%d' % (10 * i), anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)

    root.mainloop()
