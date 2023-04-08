from tkinter import *
import random

WIDTH = 700
HEIGHT = 400




PAD_W = 10

PAD_H = 100

BALL_RAD = 30
root = Tk()
root.title("Pin Pong")
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#009990")
c.pack()








c.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, fill="yellow")



BALL = c.create_oval(WIDTH/2-BALL_RAD/2,
                     HEIGHT/2-BALL_RAD/2,
                     WIDTH/2+BALL_RAD/2,
                     HEIGHT/2+BALL_RAD/2, fill="orange")

# левая ракетка
LEFT_PAD = c.create_line(PAD_W/2, 0, PAD_W/2, PAD_H, width=PAD_W, fill="black")

# правая ракетка
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 300, WIDTH-PAD_W/2, 
                          400, width=PAD_W, fill="black")

root.mainloop()
BALL_X = 20
BALL_Y = 0
 
def move_ball():
    c.move(BALL, BALL_X, BALL_Y)

SPEED = 20
# скорость левой платформы
LEFT_Rocket_SPEED = 0
# скорость правой ракетки
RIGHT_Rocket_SPEED = 0
 
