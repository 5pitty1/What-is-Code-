#   Sierpinski Triangle
#   Authour: Alan Richmond, Python3.codes

from turtle import *
size=800
min=40
pf=0.8660254

def S(l,x,y):
    if l>min:
        l=l/2
        S(l,x,y)
        S(l,x+l,y)
        S(l,x+l/2,y+l*pf)
    else:
        goto(x,y); pendown()
        begin_fill()
        forward(l); left(120)
        forward(l); left(120)
        forward(l)
        end_fill()
        setheading(0)
        penup(); goto(x,y)

penup()
speed('fastest')
S(size,-size/2,-size*pf/2.0)
done()
