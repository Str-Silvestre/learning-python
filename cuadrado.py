import turtle


window = turtle.Screen()
""" skell = turtle.Turtle()
skell.forward(50)
skell.left(90)
skell.forward(50)
skell.left(90)
skell.forward(50)
skell.left(90)
skell.forward(50)
skell.left(90)
 """

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t = turtle.Pen()
t.speed()

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

    
turtle.mainloop()

