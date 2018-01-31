
from turtle import *
import time
import random
from ball import *
import math
def white():
	bgcolor("white")
def black():
	bgcolor("black")
def pickbg():
	writer = clone()
	writer.write("if you want the background to be black, press b, white, press w ", True,font = ("Arial",30,"bold") ,align="center")
	onkey(white, "w")
	onkey(white,"W")
	onkey(black,"b")
	onkey(black,"B")
	listen()
	writer.clear()
#making a score turtle
score = clone()
score.pencolor("goldenrod")
score.color("goldenrod")

score.pu()
score.goto(1050/2,625/2)

points = 0
score.pd()
score.write("Score: "+str(points), True,font = ("Arial",30,"bold") ,align="center")
#score end
#TODO: Make a new function that spawns new enemies
#smooth
tracer(0)
ht()

#global variubles
RUNNING = True
SLEEP = 0.0077

#screan variubles
setup(1280,720)
pickbg()	

SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2

#creating the food:
NUMBER_OF_FOOD = 30
FOOD = []
for i in range(NUMBER_OF_FOOD):
	#making an x position for the food
	FOOD_X = random.randint(-SCREEN_WIDTH + 10, SCREEN_WIDTH - 10)
		
	#creating y position for the food
	FOOD_Y = random.randint(-SCREEN_HEIGHT + 10, SCREEN_HEIGHT - 10)

	#creating a color:
	FOOD_COLOR = (random.random(), random.random(), random.random())
	food = Food(FOOD_X, FOOD_Y,10, FOOD_COLOR)
	FOOD.append(food)

def spawn_food():

	#making an x position for the food
	FOOD_X = random.randint(-SCREEN_WIDTH + 10, SCREEN_WIDTH - 10)
		
	#creating y position for the food
	FOOD_Y = random.randint(-SCREEN_HEIGHT + 10, SCREEN_HEIGHT - 10)

	#creating a color:
	FOOD_COLOR = (random.random(), random.random(), random.random())
	food = Food(FOOD_X, FOOD_Y,10, FOOD_COLOR)
	FOOD.append(food)



#end of creating the food
#the playe1.5
MY_BALL = Ball(0,0,5,12,20,"green")

NUMBER_OF_BALLS = 6
MINIMUM_BALL_RADIUS = MY_BALL.r*0.75
MAXIMUM_BALL_RADIUS = MY_BALL.r*1.5
MINIMUM_BALL_DX = -1
MAXIMUM_BALL_DX = 1
MINIMUM_BALL_DY = -1
MAXIMUM_BALL_DY = 1


#balls list
BALLS = []

def win():
	for i in BALLS:
		i.ht()
		BALLS.remove(i)
		i.clear()
	for i in FOOD:
		i.ht()
		FOOD.remove(i)
		i.clear()
	MY_BALL.ht()
	score.ht()
	score.pu()
	score.goto(0,0)
	score.pd()
	score.st()
	score.clear()
	score.write("You won!", True,font = ("Garuda",50,"bold") ,align="center")
	score.ht()
	score.pu()
	score.goto(0,-50)
	score.pencolor("orangered")
	score.color("orangered")
	score.pd()
	score.st()
	score.write("coder: Noam Globerman", True,font = ("DejaVuSerif",30,"bold") ,align="center")

	score.ht()
	score.pu()
	score.goto(0,-100)
	
	score.pd()
	score.st()
	score.write("insperation: Dan Wrecker", True,font = ("DejaVuSerif",25,"bold") ,align="center")
	score.color("mediumaquamarine")
	score.pencolor("mediumaquamarine")
	score.ht()
	score.pu()
	score.goto(-SCREEN_WIDTH + 70 , -SCREEN_HEIGHT )
	score.st()
	score.pd()
	score.write("Score: " + str(points), True,font = ("Arial",20,"bold") ,align="center")

	time.sleep(5)
	quit()


#for loop the goes through number of balls

for i in range(NUMBER_OF_BALLS):
	while True:

		#creating x position for the balls
		BALLS_X = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		
		#creating y position for the balls
		BALLS_Y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		if MY_BALL.distance(BALLS_X,BALLS_Y) > MY_BALL.r*2:
			break
	#creating the balls' dx
	while True:
		BALLS_DX = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		if BALLS_DX != 0:
			break
	#creating balls's dy
	while True:
		BALLS_DY = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
		if BALLS_DY != 0:
			break
	#creating balls' radius
	BALLS_RADIUS = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	#choosing a color
	BALLS_COLOR = (random.random(), random.random(), random.random())
	#creating the actual ball
	AIBALL = Ball(BALLS_X,BALLS_Y,BALLS_DX,BALLS_DY,BALLS_RADIUS,BALLS_COLOR)
	BALLS.append(AIBALL)

def spawn():

	while True:

		#creating x position for the balls
		BALLS_X = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		
		#creating y position for the balls
		BALLS_Y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		if MY_BALL.distance(BALLS_X,BALLS_Y) > 0:
			break
	#creating the balls' dx
	while True:
		BALLS_DX = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		if BALLS_DX != 0:
			break
	#creating balls's dy
	while True:
		BALLS_DY = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
		if BALLS_DY != 0:
			break
	#creating balls' radius
	BALLS_RADIUS = random.randint(MINIMUM_BALL_RADIUS, int(MY_BALL.r*2))
	#choosing a color
	BALLS_COLOR = (random.random(), random.random(), random.random())
	#creating the actual ball
	NEWAIBALL = Ball(BALLS_X,BALLS_Y,BALLS_DX,BALLS_DY,BALLS_RADIUS,BALLS_COLOR)
	BALLS.append(NEWAIBALL)












#end of the function		
#collusion function
def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	#calculating the distance
	distance_x = ball_a.x - ball_b.x
	distance_y = ball_a.y - ball_b.y
	distance = math.sqrt(math.pow(distance_y,2)+math.pow(distance_x,2))
	#checking collusion
	if distance + 10 < ball_a.r + ball_b.r:
		return True
	else:
		return False

#function of moving the balls
def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)


#checking collisions between all balls
listpos_a = 0
listpos_b = 0
def check_all_balls_collision():
	global listpos_b, listpos_a
	while True:
		BAXCor = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		BAYCor = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		if MY_BALL.distance(BAXCor, BAYCor) > MY_BALL.r*2:
			break
	while True:
		BADX = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		if BADX != 0:
			break
	while True:
		BADY = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
		if BADY != 0:
			break
	BARadius = random.randint(MINIMUM_BALL_RADIUS, int(MY_BALL.r*2))
	BAColor = (random.random(), random.random(), random.random())
	for ball_a in BALLS:
			

		for ball_b in BALLS:
			is_b = False
			if collide(ball_a,ball_b) == True:
				BALL_A_R = ball_a.r
				BALL_B_R = ball_b.r
				if BALL_A_R > BALL_B_R:
					ball_b.x = BAXCor
					ball_b.y = BAYCor
					ball_b.dx = BADX
					ball_b.dy = BADY
					ball_b.color = BAColor
					ball_a.r += ball_b.r / 5
					ball_a.shapesize(ball_a.r/10)
					ball_b.shapesize(ball_a.r/10)
					ball_b.ht()
					ball_b.goto(ball_a.x,ball_a.y)
					ball_b.st()
				elif BALL_A_R < BALL_B_R:
					ball_a.x = BAXCor
					ball_a.y = BAYCor
					
					ball_a.dx = BADX
					ball_a.dy = BADY
					ball_a.color = BAColor
					ball_a.r = BARadius
					ball_b.r += ball_b.r / 5
					ball_b.shapesize(ball_b.r/10)

					ball_a.shapesize(ball_a.r/10)
					ball_a.ht()
					ball_a.goto(ball_a.x,ball_a.y)
					ball_a.st()
					



			listpos_b += 1		
		listpos_a += 1
def check_myball_collision():
	global points
#bots renweing stats vars
	while True:
		BAXCor = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
		BAYCor = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
		if MY_BALL.distance(BAXCor, BAYCor) > MY_BALL.r*2:
			break
	while True:
		BADX = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		if BADX != 0:
			break
	while True:
		BADY = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
		if BADY != 0:
			break
	BARadius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	BAColor = (random.random(), random.random(), random.random())
	for i in FOOD:
		if collide(MY_BALL,i) == True:
			spawn_food()
			i.ht()
			FOOD.remove(i)
			i.clear()
			MY_BALL.r += 0.25
			MY_BALL.shapesize(MY_BALL.r/10)
			######################
			#making the score turtle
			points += 1
			score.clear()
			score.pu()
			
			score.goto(1050/2,625/2)

			score.pd()
			score.write("Score: "+str(points), True,font = ("Arial",30,"bold") ,align="center")
			if MY_BALL.r >= 250:
				win()
	#going through the balls list
	for i in BALLS:
		global NUMBER_OF_BALLS
		#checking if there is a collision between the player to a bot
		if collide(i,MY_BALL):
			coludedBallR = i.r
			if coludedBallR > MY_BALL.r:
				lose()

				return False
			else:
				# while True:
				# 	i.ht()
				# 	#creating x position for the balls
				# 	BALLS_X = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
					
				# 	#creating y position for the balls
				# 	BALLS_Y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				# 	if MY_BALL.distance(BALLS_X,BALLS_Y) > 0:
				# 		i.goto(BAXCor, BAYCor)
				# 		i.st()
				# 		break
				
				# i.dx = BADX
				# i.dy = BADY
				# # i.r = BARadius
				# i.color = BAColor
				# i.shapesize(i.r/10)
				i.ht()
				BALLS.remove(i)	
				spawn()
				MY_BALL.r += 5
				MY_BALL.shapesize(MY_BALL.r/10)


	return True
VecSpeed = 100.0
#making the player move by hovering with the mouse function
def movearound():
	global VecSpeed
	#getting the position of the mouse and saving it as the new player positions
	old_x = MY_BALL.x
	old_y = MY_BALL.y
	mouse_x = getcanvas().winfo_pointerx() - SCREEN_WIDTH
	mouse_y = (-getcanvas().winfo_pointery() + SCREEN_HEIGHT)
	MY_BALL.dvx = MY_BALL.dx*((mouse_x - old_x)/VecSpeed)
	MY_BALL.dvy = MY_BALL.dy*((mouse_y - old_y)/VecSpeed)
	# MY_BALL.dvx = ((mouse_x - old_x)/250.0)
	# MY_BALL.dvy = ((mouse_y - old_y)/250.0)

	print(str(mouse_y))


def lose():
	MY_BALL.ht()
	score.ht()
	score.pu()
	score.goto(0,0)
	
	score.st()
	score.pd()
	score.clear()
	score.write("You lost!", True,font = ("Garuda",40,"bold") ,align="center")
	score.ht()
	score.pu()
	score.goto(-10,-50)
	score.pencolor("orangered")
	score.color("orangered")
	score.pd()
	score.st()
	score.write("coder: Noam Globerman", True,font = ("DejaVuSerif",30,"bold") ,align="center")
	score.ht()
	score.pu()
	score.goto(0,-100)
	
	score.pd()
	score.st()
	score.write("insperation: Dan Wrecker", True,font = ("DejaVuSerif",25,"bold") ,align="center")
	score.color("mediumaquamarine")
	score.pencolor("mediumaquamarine")
	score.ht()
	score.pu()
	score.goto(-SCREEN_WIDTH + 70 , -SCREEN_HEIGHT )
	score.st()
	score.pd()
	score.write("Score: " + str(points), True,font = ("Arial",20,"bold") ,align="center")
	
	time.sleep(6)
	quit()
	
	

while RUNNING:
	
	move_all_balls()
	movearound()
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)

	check_all_balls_collision()
	check_myball_collision()
	
	getscreen().update()
	time.sleep(0.01)
		

mainloop()