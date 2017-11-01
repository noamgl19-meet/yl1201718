import turtle
turtle.setup(800,800)
turtle.ht()
turtle.pu()
turtle.goto(0,0)
turtle.pd()
middle_x = 0
middle_y = 0
bigradius = 100
smallradius = 50
turtle.pu()
turtle.goto(0,-smallradius)
turtle.pd()
turtle.circle(smallradius)
turtle.pu()
turtle.goto(0,-bigradius)
turtle.pd()
turtle.circle(bigradius)
def drawTriangle():
	turtle.pd()
	turtle.goto(middle_x,middle_y)
	turtle.forward(smallradius)
	turtle.left(36)
	turtle.forward(smallradius)
	turtle.goto(middle_x,middle_y)

for i in range(10):
	drawTriangle()


turtle.mainloop()