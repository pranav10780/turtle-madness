import turtle
hex = turtle.Pen()
color =['red', 'purple','blue','green','orange','yellow']
turtle.bgcolor('black')
for i in range(360):
    hex.pencolor(color[i % 6])
    hex.width(i/100+1)
    hex.forward(i)
    hex.left(59)