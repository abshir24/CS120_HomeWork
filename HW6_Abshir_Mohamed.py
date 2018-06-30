import turtle

window1 = turtle.Screen()

window1.bgcolor("black")

window1.title("shapes")

pen=turtle.Turtle()

pen.setposition(-500, 100)

pen.color("red")

pen.pendown()

pen.begin_fill()
def shape(t,s,sh):
    count = 0;
    for x in range(sh):
        if count%2==0:
            t.forward(s)
            t.right(360/sh)
        else:
            t.forward(s/2)
            t.right(360/sh)
        count+=1

shape(pen,800,4)

pen.setposition(0,300)

pen.setposition(300,100)

pen.end_fill()

pen.penup()

pen.color("turquoise")

pen.setposition(0,0)

pen.pendown()
pen.begin_fill()
shape(pen,200,4)
pen.end_fill()
pen.pensize(3)
pen.color("black")
pen.setposition(200,0)
pen.setposition(200,-100)
pen.setposition(0,-100)
pen.setposition(0,0)
pen.setposition(100,0)
pen.setposition(100,-50)
pen.setposition(200,-50)
pen.setposition(100,-50)
pen.setposition(0,-50)
pen.setposition(100,-50)
pen.setposition(100,-100)
pen.penup()
pen.setposition(-400,0)
pen.pendown()
pen.color("turquoise")
pen.pensize(0)
pen.begin_fill()
shape(pen,200,4)
pen.end_fill()
pen.color("black")
pen.pensize(3)
pen.setposition(-200,0)
pen.setposition(-200,-100)
pen.setposition(-400,-100)
pen.setposition(-400,0)
pen.setposition(-300,0)
pen.setposition(-300,-50)
pen.setposition(-200,-50)
pen.setposition(-300,-50)
pen.setposition(-400,-50)
pen.setposition(-300,-50)
pen.setposition(-300,-100)
pen.penup()
pen.setposition(-150,-150)

pen.color("turquoise")
def shape2(t,s,sh):
    count = 0;
    for x in range(sh):
        if count%2==0:
            t.forward(s)
            t.right(360/sh)
        else:
            t.forward(s+50)
            t.right(360/sh)
        count+=1


pen.begin_fill()
shape2(pen,100,4)
pen.end_fill()

pen.color("black")
pen.pensize(3)
pen.pendown()
shape2(pen,100,4)
pen.penup()
pen.setposition(-130,-225)
pen.color("gold")
pen.begin_fill()
pen.circle(7)
pen.end_fill()
pen.setposition(0,0)
