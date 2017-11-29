from turtle import *
import random
colormode(255)
class Hexagon(Turtle):
	def __init__(self,size, speed):
		Turtle.__init__(self)
		self.ht()
		self.pu()

		register_shape("hexagon", ((50,0),(75,25),(50,50),(25,50),(0,25),(25,0)))
		
		self.shapesize(size)
		self.speed(speed)
		
		
		self.shape("hexagon")
	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

		self.color(r, g, b)

hexa1 = Hexagon(1,7)
hexa1.right(90)
hexa1.st()
hexa1.random_color()
hexa1.goto(50,50)
mainloop()