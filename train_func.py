import turtle
import math




def draw_vagon():
    draw_box(100,150)
    t.backward(2)
    t.speed(0)
    t.left(90)
    circle(50)
    t.left(90)
    t.setheading(0)
    t.backward(25)
    t.left(90)
    circle(25)
    t.penup()
    t.forward(100)
    t.left(90)
    t.forward(40)
    t.setheading(0)
    t.pendown()
    draw_box(40,30)
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()
    t.forward(15)


def  draw_right_triangle(s1,s2):
    t.forward(s1)
    t.left(90)
    t.forward(s2)
    t.left(90+math.degrees(math.asin(s2/math.sqrt(s1*s1+s2*s2))))
    t.forward(math.sqrt(s1*s1+s2*s2))
    # t.left(90+math.degrees(math.asin(s2/math.sqrt(s1*s1+s2*s2))))
    

def draw_box(s1,s2):
    t.forward(s1)
    t.left(90)
    t.forward(s2)
    t.left(90)
    t.forward(s1)
    t.left(90)
    t.forward(s2)
    t.left(90)
    t.forward(s1)
def circle(s1):
    t.circle(s1)


t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)

t.speed(0)
draw_right_triangle(100,100)
t.setheading(0)
t.forward(100)
draw_box(150,100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(75)

t.setheading(0)
draw_box(20,50)
t.left(90)

t.forward(50)
t.left(90)
t.forward(30)
t.setheading(0)
t.speed(0)

draw_box(40,20)
t.right(90)
t.penup()
t.forward(200)
t.left(90)
t.pendown()
circle(25)
t.pendown()
t.penup()
t.backward(80)
t.pendown()
circle(25)

#tekerbitti
t.penup()

t.forward(130)
t.left(90)
t.forward(50)
t.pendown()

t.setheading(0)
draw_box(100,150)
t.backward(2)
t.speed(0)
t.left(90)
circle(50)
t.left(90)
t.setheading(0)
t.backward(25)
t.left(90)
circle(25)
t.penup()
t.forward(100)
t.left(90)
t.forward(40)
t.setheading(0)
t.pendown()
draw_box(40,30)
t.penup()
t.forward(30)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()
t.forward(15)
#vagonbegin
draw_vagon()
draw_vagon()
draw_vagon()
draw_vagon()
draw_vagon()
draw_vagon()


turtle.done()
