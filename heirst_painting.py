# Heirst painting using python turtle

import turtle
from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()
timmy_the_turtle.color("DarkGreen")
turtle.colormode(255)
timmy_the_turtle.pensize(1)
timmy_the_turtle.speed("fastest")


def color_change():
    color = random.choice(color_list)
    return timmy_the_turtle.color(color)
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.setx(-180)
timmy_the_turtle.sety(-180)
timmy_the_turtle.pendown()
pos = timmy_the_turtle.pos()

def draw_dot(radius):
    return timmy_the_turtle.dot(radius)


color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123),
              (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81)]


def draw_dot_row():
    timmy_the_turtle.pendown()
    color_change()
    draw_dot(20)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(50)


def next_row():
    global pos
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(50)
    pos = timmy_the_turtle.position()
    timmy_the_turtle.setposition(pos)
    timmy_the_turtle.setheading(0)


def draw_painting():

    for i in range(10):
        draw_dot_row()
    timmy_the_turtle.setposition(pos)
    next_row()

w=1
while w <= 10:
    draw_painting()
    w+=1


screen = Screen()
screen.exitonclick()

