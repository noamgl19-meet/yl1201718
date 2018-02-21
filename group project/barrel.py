
from turtle import *
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
left_edge = -SCREEN_WIDTH/2 + 50
right_edge = SCREEN_WIDTH/2 - 50
class Barrel(Turtle):

	def __init__(self,is_special):

		Turtle.__init__(self)
		self.is_special = is_special

		self.x = SCREEN_WIDTH/2 -30
		self.y = 360
		self.r = 5

		# dont forget to set the shape to the crawling shape

	def crawl(self):
		self.pu()
		self.speed(1)
		self.goto(right_edge + 50,95)
		
		self.goto(left_edge + 50,45)
		self.goto(left_edge + 50, -5)

	def next(floors,i):

		while(floors[i+1].get_y(SCREEN_WIDTH- self.crawling_shape_r) != self.ycore()):

			self.y -= 1
			self.goto(self.x,self.y)

		# dont forget to change the shape to the crawling_shape

