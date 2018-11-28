from tkinter import *
import time
import random as ran

yo = Tk()

yo.title("NJ Game")

canvas = Canvas(yo, height="500", width="500", bd=0, highlightthickness=0, bg='black')

canvas.pack()


class Star:
    def __init__(self, can, color):
        self.canvas = can
        self.id = can.create_text(250, 250, text="*", fill=color, font=("Times", 26))
        self.turn = 0
        self.mx = 0
        self.my = 0
        self.speed = 5
        self.pos = 0
        self.canvas.bind_all('<KeyPress-Up>', self.up)
        self.canvas.bind_all('<KeyPress-Down>', self.down)
        self.canvas.bind_all('<KeyPress-Right>', self.right)
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.fx = ran.randint(10, 480)
        self.fy = ran.randint(10, 480)
        self.fid = can.create_text(self.fx, self.fy, text="@", fill="cyan", font=("Times", 20))
        self.score = 0
        self.shows = can.create_text(10, 10, text=self.score, fill="yellow", font=("Times", 20))

    def create_food(self):
        self.canvas.move(self.fid, -self.fx, -self.fy)
        self.fx = ran.randint(10, 480)
        self.fy = ran.randint(10, 480)
        print(self.fx, " ", self.fy)
        self.canvas.move(self.fid, self.fx, self.fy)
        self.score += 1
        self.canvas.itemconfig(self.shows, text=self.score)
        if self.score == 10:
            self.speed = 8
        elif self.speed == 15:
            self.speed = 12
        elif self.score == 20:
            self.speed = 15

    def check(self):
        if 5 >= self.fx - self.pos[0] >= -15 and 5 >= self.fy - self.pos[1] >= -15:
            self.create_food()

    def up(self, evt):
        self.turn = 1

    def down(self, evt):
        self.turn = 2

    def right(self, evt):
        self.turn = 3

    def left(self, evt):
        self.turn = 4

    def draw(self):
        self.canvas.move(self.id, self.mx, self.my)
        self.pos = self.canvas.coords(self.id)
        # for up
        if self.turn == 1:
            self.my = -self.speed
            self.mx = 0
        # down
        elif self.turn == 2:
            self.my = self.speed
            self.mx = 0
        #       right
        elif self.turn == 3:
            self.mx = self.speed
            self.my = 0
        #         left
        elif self.turn == 4:
            self.mx = -self.speed
            self.my = 0

        if self.pos[0] <= 5:
            self.canvas.move(self.id, 489, self.my)
        elif self.pos[0] >= 490:
            self.canvas.move(self.id, -489, self.my)

        if self.pos[1] <= 5:
            self.canvas.move(self.id, self.mx, 489)
        elif self.pos[1] >= 490:
            self.canvas.move(self.id, self.mx, -489)


star = Star(canvas, "red")

while 1:
    star.draw()
    star.check()
    yo.update_idletasks()
    yo.update()
    time.sleep(0.01)
