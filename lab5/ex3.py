from turtle import *
import random
SIZE_X = 1080
SIZE_Y = 720
setup(SIZE_X,SIZE_Y)
writer = Turtle()
writer.pu()
writer.ht()
colormode(255)
class Hexagon(Turtle):
	def __init__(self,size, speed, pencolor, fillcolor):
		Turtle.__init__(self)
		self.ht()
		self.pu()

		begin_poly()
		pu()
		ht()
		
		goto(50,0)
		goto(75,25)
		goto(50,50)
		goto(25,50)
		goto(0,25)
		goto(25,0)
		self.right(90)
		st()
		pd()
		end_poly()
		hexashape = get_poly()
		register_shape("hexagon", hexashape)
		self.shapesize(size)
		self.speed(speed)
		self.pencolor(pencolor)
		
		ht()
		self.shape("hexagon")
	# def random_color(self):
	# 	r = random.randint(0,255)
	# 	g = random.randint(0,255)
	# 	b = random.randint(0,255)
	
		self.fillcolor(fillcolor)

hexa1 = Hexagon(1,5, "red", "maroon")
hexa1.ht()
hexa1.goto(50,50)
hexa2 = Hexagon(3,6,"black","green")
hexa2.st()
hexa2.goto(-50,-50)
writer.goto(-160,-50)
writer.pd()

writer.write("dogs", True, align="center")
hexa3 = Hexagon(1,5,"orange","brown")
hexa3.st()
hexa3.goto(50,50)
writer.goto(20,50)
writer.pd()

writer.write("animals", True, align="center")
writer.pu()
writer.goto(13,50)
writer.pd()
hexa4 = Hexagon(3,6,"black","green")
hexa4.st()
hexa4.goto(275,-50)
writer.goto(165,-50)
writer.pd()

writer.write("cats", True, align="center")
mainloop()