
import turtle
turtle.colormode(255)
turtle.bgcolor(0,0,0)   #sets bg color
bob=turtle.Turtle()
bob.speed(0)
for times in range(500):#sets how many iterations
    bob.begin_fill()
    bob.color(0,0,255)  #sets pen color green
    bob.circle(360)
    bob.right(500)
    bob.circle(800)     #radius of circle
    bob.penup
    bob.goto(0,0)       #cordinate of (0,0)
    bob.pendown
    bob.color(0,255,0)  #sets pen color blue
    bob.circle(360)     #radius of circle
    bob.left(90)        #90 degree angle
    bob.forward(200)
