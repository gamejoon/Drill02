from pico2d import *

open_canvas()

import os
os.chdir("D:\\2DGP\\Drill02")

grass = load_image('grass.png')
character = load_image("character.png")

import math

x = 400
y = 90

move_shape = ["square", "circle"]
now_shape = move_shape[1]

def draw_picture(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def move_square():
    global x, y
    while(x < 800):
        x += 2
        draw_picture(x, y)

    while(y < 600):
        y += 2
        draw_picture(x, y)

    while (x > 0):
        x -= 2
        draw_picture(x, y)

    while (y > 90):
        y -= 2
        draw_picture(x, y)

    while (x < 400):
        x += 2
        draw_picture(x, y)

def move_circle():
    global x, y
    theta = 270
    while(theta > -90):
        theta -= 1
        x = math.cos(theta * math.pi / 180) * 250 + 400
        y = (math.sin(theta * math.pi / 180) + 1) * 250 + 90
        draw_picture(x, y)

while (1):
    
    if now_shape == "square":
        move_square()
        now_shape = move_shape[1]
    elif now_shape == "circle":
        move_circle()
        now_shape = move_shape[0]

close_canvas()
