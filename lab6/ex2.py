from turtle import *
import random
colormode(255)
class Hexagon(Turtle):
	def __init__(self,size):
		realsize = size*10
		Turtle.__init__(self)
		self.ht()
		begin_poly()
		self.goto(realsize,0)
		self.goto(realsize*1.5,realsize/2)
		self.goto(realsize,realsize)
		self.goto(0,realsize)
		self.goto(-realsize/2, realsize/2)
		self.goto(0,0)
		end_poly()
		self.st()
		shape = get_poly()
		register_shape("shape", shape)
		self.shape("shape")
hexa1 = Hexagon(5)
hexa1.goto(50,50)

mainloop()