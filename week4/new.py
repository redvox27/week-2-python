from tkinter import *
from random import randint
import time

class Graph :
    s = 1
    x2 = 50;
    y2 = 0;
    running = False;
    maxValue = 100
    minValue = 0

    def __init__(self,master):

        self.y2 = self.value_to_y(randint(self.minValue,self.maxValue))
        self.master = master

        master.title("plot")


        self.canvas = Canvas(root, width=1200, height=600, bg='white') # 0,0 is top left corner
        self.canvas.pack(expand=YES, fill=BOTH)

        Button(root, text='Quit', command=root.quit).pack()
        Button(root,text="Run", command=self.start).pack()
        Button(root,text="pause",command=self.stop).pack()
        Button(root,text="resume",command=self.resume).pack()

        labelx = Label(root,text = "step")
        labelx.place(x=1000, y = 570)

        labely = Label(root,text = "value")
        labely.place(x = 5,y = 210 )

        maxLable = Label(root, text = "max value")
        maxLable.pack()
        self.maxEntry = Entry(root)
        self.maxEntry.pack()

        minLable = Label(root, text="min value")
        minLable.pack()
        self.minEntry = Entry(root)
        self.minEntry.pack()

        Button(root, text="set", command=self.set).pack()

        self.canvas.create_line(50,550,1150,550, width=2) # x-axis
        self.canvas.create_line(50,550,50,50, width=2)    # y-axis



        for i in range(23):
            x = 50 + (i * 50)
            self.canvas.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.canvas.create_text(x, 550, text='%d' % (10 * i), anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)



    def value_to_y(self,value):
        return 550-5*value

    def start(self):
        self.running = True
        self.step()

    def stop(self):
        self.running = False

    #moet op resume drukken om running weer nul te maken, dan pas kan je weer op run klikken
    def resume(self):
        self.running = True
        self.step()

    def set(self):
        self.minValue = self.minEntry.getint();
        self.maxValue = self.maxEntry.getint();




    def step(self):
        if self.running:

            if self.s == 23:
                # new frame
                self.s = 1
                self.x2 = 50


                self.canvas.delete('temp') # only delete items tagged as temp

            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s*50
            self.y2 = self.value_to_y(randint(0,100))

            self.canvas.create_line(x1, y1, self.x2, self.y2, fill='blue', tags='temp')
            #print(s, x1, y1, x2, y2)
            self.s += 1;


            self.canvas.after(300, self.step)





root = Tk()
gui = Graph(root)
root.mainloop()