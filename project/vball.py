from turtle import *
# #screan setup
# SIZE_X = getcanvas().winfo_width()*2
# SIZE_Y = getcanvas().winfo_height()*2
# setup(SIZE_X,SIZE_Y)
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
		new_x = current_x + self.dx
		#getting the current y
		current_y = self.y
		#getting the new y position(the last y position + dy)
		new_y = current_y + self.dy
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
		self.x = new_x
		self.y = new_y
		self.goto(new_x,new_y)

		# checking if it is out of borders
		if right_side_ball >= screen_width:
			self.dx = -self.dx
		if left_side_ball <= -screen_width:
			self.dx = -self.dx
		if top_side_ball >= screen_height:
			self.dy = -self.dy
		if bottom_side_ball <= -screen_height:
			self.dy = -self.dy
