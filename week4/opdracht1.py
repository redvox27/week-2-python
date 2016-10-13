from tkinter import *
from random import randint
import time

class Graph:



    def __init__(self):
        self.root = Tk()
        self.root.title('simple plot')

        self.canvas = self.canvas(self.root, width=1200, height=600, bg='white')  # 0,0 is top left corner
        self.canvas.pack(expand=YES, fill=BOTH)

        Button(self.root, text='Quit', command=self.root.quit).pack()

        self.canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis
        self.canvas.create_line(50, 550, 50, 50, width=2)  # y-axis


    def value_to_y(val):
            return 550 - 5 * val


    # init global vars
    s = 1
    x2 = 50
    y2 = value_to_y(randint(0, 100))

    def step(self):
        global s, x2, y2
        if s == 23:
            # new frame
            s = 1
            x2 = 50
            self.canvas.delete('temp')  # only delete items tagged as temp
        x1 = x2
        y1 = y2
        x2 = 50 + s * 50
        y2 = value_to_y(randint(0, 100))
        canvas.create_line(x1, y1, x2, y2, fill='blue', tags='temp')
        # print(s, x1, y1, x2, y2)
        s = s + 1
        canvas.after(300, step)

    def draw(self):


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

            self.canvas.after(300)
            self.root.mainloop()

graph = Graph()
graph.draw()