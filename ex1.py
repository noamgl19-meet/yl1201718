from turtle import *
import random
import math
circles = []
randpos = random.randint(-250,250)
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
circle1 = Ball(20,"red", 7)
circles.append(circle1)
circle1.goto(100,100)
circle2 = Ball(30,"blue", 5)
circles.append(circle2)
circle2.goto(-100,96)
circle3 = Ball(35,"orange", 7)
circles.append(circle3)
circle3.goto(-100,96)
# def check_collision(circle1,circle2):
# 	x = circle2.xcor() - circle1.xcor()
# 	new_x = math.pow(x,2)
# 	y = circle2.ycor() - circle1.ycor()
# 	new_y = math.pow(y,2)
# 	sum = math.sqrt(new_x + new_y)
# 	if sum <= circle1.radius + circle2.radius:
# 		print("colide")
		
# 	else:
# 		print("not colide")
# check_collision(circle2,circle1)
def pair_collisions(circles):
	for x in circles:
		for y in circles:
			if x != y:
				xpos = y.xcor() - x.xcor()
				new_x = math.pow(xpos,2)
				ypos = y.ycor() - x.ycor()
				new_y = math.pow(ypos,2)
				sum = math.sqrt(new_x + new_y)
				if sum <= x.radius + y.radius:
					print("there was a collision")
					y.goto(randpos, randpos)
					break
				else:
					print("no collision")
pair_collisions(circles)
mainloop()