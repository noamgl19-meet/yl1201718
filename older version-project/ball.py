from turtle import *
# #screan setup
# SIZE_X = getcanvas().winfo_width()*2
# SIZE_Y = getcanvas().winfo_height()*2
# setup(SIZE_X,SIZE_Y)

#class of food begin:
class Food(Turtle):
	def __init__(self, x, y, r, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		self.r = r
		
		
		self.shapesize(r/10)
		self.x = x
		self.y = y
		self.color(color)
		self.fillcolor(color)
		self.goto(x,y)

#main class

class Ball(Turtle):
	#x = x position
	#y = y position
	#dx, dy = the speed towards x or y
	#r = radius
	#color = color
	def __init__(self, x, y, dx, dy, r, color):
		#making sure we inheret from turtle
		Turtle.__init__(self)
		#pen up so we can set the starting position
		pu()
		self.pu()
		self.goto(x,y)
		self.x = x
		self.y = y
		#ddeclairing the other atributes
		self.dx = dx
		self.dy = dy
		self.dvx = dx
		self.dvy = dy
		self.r = r
		#setting the shape to a circle
		self.shape("circle")
		#setting the shapesize to r/10 because a point is 20 pixles,
		#and a radius is half koter
		self.shapesize(r/10)
		#coloring the object
		self.color(color)
		self.fillcolor(color)
	#moving the circle method
	def move(self, screen_width, screen_height):

		#getting the current x
		current_x = self.x
		#getting the new x position(the last position + the dx)
		new_x = current_x + self.dvx
		self.x = new_x

		#getting the current y
		current_y = self.y
		#getting the new y position(the last y position + dy)
		new_y = current_y + self.dvy
		self.y = new_y

		#getting the sides of the ball
		#right
		right_side_ball = new_x + self.r
		#left
		left_side_ball = new_x - self.r
		#up
		top_side_ball = new_y + self.r
		#down
		bottom_side_ball = new_y - self.r
		#going to the new cordination

		# checking if it is out of borders
		if right_side_ball >= screen_width:
			self.dvx = -self.dvx
		if left_side_ball <= -screen_width:
			self.dvx = -self.dvx
		if top_side_ball >= screen_height:
			self.dvy = -self.dvy
		if bottom_side_ball <= -screen_height:
			self.dvy = -self.dvy
			
		self.goto(new_x,new_y)
