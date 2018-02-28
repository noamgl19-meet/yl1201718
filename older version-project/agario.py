

from turtle import *
import time
import random
from ball import *
import math
<<<<<<< HEAD:older version-project/agario.py
#smooth
tracer(0)
ht()
#making a score turtle
score = clone()
score.pencolor("red")
score.color("red")
score.pu()
score.goto(1050/2,625/2)

points = 0
score.pd()
score.write("Score: "+str(points), True,font = ("Arial",30,"bold") ,align="center")
#score end
#global variubles
RUNNING = True
SLEEP = 0.0077

#screan variubles
setup(1280,720)
=======
title("BAGAR IO")
writing = clone()
>>>>>>> c1ebf657dbac09d837697ce39e43092545610bce:project/agario.py
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2
score_X = SCREEN_WIDTH +10
score_Y = SCREEN_HEIGHT - 5
points = 0
def main():
	global score_X,score_Y
	clearscreen()
	clear()

	#title
	title("Bagar io - all rights reserved to @noamgloberman 2018")
	#colors of the background
	def maroon():
		bgcolor("maroon")
	def white():
		bgcolor("white")
	def black():
		bgcolor("black")
	def yellow():
		bgcolor("yellowgreen")
	def grey():
		bgcolor("grey")
	def silver():
		bgcolor("silver")
	def pickbg():
		writer = clone()
		onkey(white, "w")
		onkey(white,"W")
		onkey(black,"b")
		onkey(black,"B")
		onkey(maroon,"m")
		onkey(maroon,"M")
		onkey(yellow,"y")
		onkey(yellow,"Y")
		onkey(silver,"s")
		onkey(silver,"S")
		onkey(grey,"g")
		onkey(grey,"G")

<<<<<<< HEAD:older version-project/agario.py
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
#the player
MY_BALL = Ball(0,0,5,12,60,"green")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = MY_BALL.r * 3
MINIMUM_BALL_DX = -1
MAXIMUM_BALL_DX = 1
MINIMUM_BALL_DY = -1
MAXIMUM_BALL_DY = 1
=======
		listen()
		writer.clear()

	#making a score turtle
	score = clone()
	score.pencolor("goldenrod")
	score.color("goldenrod")

	score.pu()
	score.goto(score_X,score_Y)
>>>>>>> c1ebf657dbac09d837697ce39e43092545610bce:project/agario.py

	
	score.pd()
	score.write("Score: "+str(points),font = ("Purisa",30,"bold") ,align="center")
	#score end
	#TODO: Make a new function that spawns new enemies
	#smooth
	tracer(0)
	ht()

<<<<<<< HEAD:older version-project/agario.py
#balls list
BALLS = []
#winning function:
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
	score.goto(-50,0)
	score.pd()
	score.st()
	score.clear()
	score.write("You won!", True,font = ("Arial",50,"bold") ,align="center")
	score.ht()
	score.pu()
	score.goto(-50,-100)
	score.pd()
	score.st()
	score.write("Score: " + str(points), True,font = ("Arial",50,"bold") ,align="center")
	time.sleep(3)
	quit()
=======
	#global variubles
	RUNNING = True
	SLEEP = 0.0077

	#screan variubles
	setup(1280,720)
	pickbg()	
>>>>>>> c1ebf657dbac09d837697ce39e43092545610bce:project/agario.py

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

<<<<<<< HEAD:older version-project/agario.py
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
	BALLS_RADIUS = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	#choosing a color
	BALLS_COLOR = (random.random(), random.random(), random.random())
	#creating the actual ball
	AIBALL = Ball(BALLS_X,BALLS_Y,BALLS_DX,BALLS_DY,BALLS_RADIUS,BALLS_COLOR)
	BALLS.append(AIBALL)
##########
#spawning enemies
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
	BALLS_RADIUS = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	#choosing a color
	BALLS_COLOR = (random.random(), random.random(), random.random())
	#creating the actual ball
	NEWAIBALL = Ball(BALLS_X,BALLS_Y,BALLS_DX,BALLS_DY,BALLS_RADIUS,BALLS_COLOR)
	BALLS.append(NEWAIBALL)












#end of the function
##########		
#collusion function
def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	#calculating the distance
	distance_x = ball_a.x - ball_b.x
	distance_y = ball_a.y - ball_b.y
	distance = math.sqrt(math.pow(distance_y,2)+math.pow(distance_x,2))
	#checking collusion
	if distance + 10 <= ball_a.r + ball_b.r:
		return True
	else:
		return False
=======
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

	NUMBER_OF_BALLS = 5
	MINIMUM_BALL_RADIUS = MY_BALL.r*0.75
	MAXIMUM_BALL_RADIUS = MY_BALL.r*1.5
	MINIMUM_BALL_DX = -1
	MAXIMUM_BALL_DX = 1
	MINIMUM_BALL_DY = -1
	MAXIMUM_BALL_DY = 1


	#balls list
	BALLS = []

	def win():
		global timeScore
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
		score.write("You won!",font = ("Garuda",50,"bold") ,align="center")
		score.ht()
		score.pu()
		score.goto(0,-50)
		score.pencolor("orangered")
		score.color("orangered")
		score.pd()
		score.st()
		score.write("coder: Noam Globerman",font = ("DejaVuSerif",30,"bold") ,align="center")

		score.ht()
		score.pu()
		score.goto(0,-100)
		
		score.pd()
		score.st()
		score.write("inspiration: Dan Wrecker",font = ("DejaVuSerif",25,"bold") ,align="center")
		score.color("mediumaquamarine")
		score.pencolor("mediumaquamarine")
		score.ht()
		score.pu()
		score.goto(-SCREEN_WIDTH + 70 , -SCREEN_HEIGHT )
		score.st()
		score.pd()
		score.write("Score: " + str(points),font = ("KacstDecorative",20,"bold") ,align="center")
		aSize = 15
		bSize = 25
		cSize = 0
>>>>>>> c1ebf657dbac09d837697ce39e43092545610bce:project/agario.py

		if timeScore <= aSize:
			grade = "A+"
		elif timeScore > aSize and timeScore <= bSize:
			grade = "B+"
		elif timeScore > bSize and timeScore <= cSize:
			grade = "C+"
		else:
			grade = "F"
		score.pu()
		score.goto(0,-150)
		score.pd()
		score.write("Grade: "+grade,font = ("Purisa",25,"bold") ,align="center")
		score.color("mediumaquamarine")

		time.sleep(5)
		clear()
		score.clear()
		MY_BALL.clear()
		for i in BALLS:
			i.clear()
			i.ht()
		for i in FOOD:
			i.clear()
			i.ht()
		menu()
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
		if distance  < ball_a.r + ball_b.r:
			return True
		else:
			return False

	#function of moving the balls
	def move_all_balls():
		for i in BALLS:
			i.move(SCREEN_WIDTH,SCREEN_HEIGHT)


	#checking collisions between all balls
	
	def check_all_balls_collision():
		while True:
			BAXCor = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			BAYCor = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			if MY_BALL.distance(BAXCor, BAYCor) > MY_BALL.r*2+30:
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
						ball_b.shapesize(ball_a.r/10)
						ball_b.ht()
						ball_b.goto(ball_a.x,ball_a.y)
						ball_b.st()
						getscreen().update()
					elif BALL_A_R < BALL_B_R:
						ball_a.x = BAXCor
						ball_a.y = BAYCor
						
						ball_a.dx = BADX
						ball_a.dy = BADY
						ball_a.color = BAColor
						ball_a.r = BARadius

						ball_a.shapesize(ball_a.r/10)
						ball_a.ht()
						ball_a.goto(ball_a.x,ball_a.y)
						ball_a.st()
						getscreen().update()



<<<<<<< HEAD:older version-project/agario.py
		for ball_b in BALLS:
			is_b = False
			if collide(ball_a,ball_b) == True:
				BALL_A_R = ball_a.r
				BALL_B_R = ball_b.r
				if BALL_A_R > BALL_B_R:
					ball_b.goto(BAXCor, BAYCor)
					# ball_b.x = BAXCor
					# ball_b.y = BAYCor
					# ball_b.dx = BADX
					# ball_b.dy = BADY
					# ball_b.color = BAColor
					# ball_a.r += 1
					ball_b.ht()
					BALLS.remove(ball_b)
					spawn()
				elif BALL_A_R < BALL_B_R:
					# ball_a.x = BAXCor
					# ball_a.y = BAYCor
					# ball_a.goto(BAXCor, BAYCor)
					# ball_a.dx = BADX
					# ball_a.dy = BADY
					# ball_a.color = BAColor
					# ball_b.r = ball_b.r + 1
					ball_a.ht()
					BALLS.remove(ball_a)
								
					
					spawn()			
					
def check_myball_collision():
	global NUMBER_OF_BALLS, points

	#bots renweing stats vars
	BAXCor = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	BAYCor = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
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
			if MY_BALL.r >= 300:
				win()
	#going through the balls list
	for i in BALLS:
		#checking if there is a collision between the player to a bot
		if collide(i,MY_BALL):
			coludedBallR = i.r
			if coludedBallR > MY_BALL.r:
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
				MY_BALL.r += i.r/10
				MY_BALL.dx = MY_BALL.dx / 2
				MY_BALL.dy = MY_BALL.dy / 2
				i.ht()
				BALLS.remove(i)	
				i.clear()

				spawn()
				NUMBER_OF_BALLS +=1
				MY_BALL.shapesize(MY_BALL.r/10)
				######################
				#making the score turtle
				points += 10
				score.clear()
				score.pu()
				score.goto(1050/2,625/2)

				score.pd()
				score.write("Score: "+str(points), True,font = ("Arial",30,"bold") ,align="center")

				if MY_BALL.r >= 300:
					win()
					
				#end of score
				######################

	return True
#making the player move by hovering with the mouse function
def movearound(event):
#getting the position of the mouse and saving it as the new player positions
	old_x = MY_BALL.x
	old_y = MY_BALL.y
	MY_BALL.x = event.x - SCREEN_WIDTH
	MY_BALL.y = SCREEN_HEIGHT - event.y
	smooth_x = old_x + 0.9 * math.fabs(MY_BALL.x - old_x)
	smooth_y = old_y + 0.9 * math.fabs(MY_BALL.y - old_y)
	MY_BALL.goto(smooth_x,smooth_y)
		
getcanvas().bind("<Motion>", movearound)
cond = 0
counter = 0
while RUNNING:
	time.sleep(0.01)

	move_all_balls()
	check_all_balls_collision()
	#checking time:
	if counter == 0:
		while cond < 100:
			print(cond)
			cond += 1
	counter = 1
	if cond > 99:
		if check_myball_collision() == False:
			write("You lost", True,font = ("Arial",50,"bold") ,align="center")
			time.sleep(3)
			quit()
			RUNNING = False
	getscreen().update()
	
=======
				
	def check_myball_collision():
		global points
	#bots renweing stats vars
		while True:
			BAXCor = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			BAYCor = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			if MY_BALL.distance(BAXCor, BAYCor) > MY_BALL.r*2+30:
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
				
				score.goto(score_X,score_Y)

				score.pd()
				score.write("Score: "+str(points),font = ("Purisa",30,"bold") ,align="center")
				getscreen().update()
		#going through the balls list
		for i in BALLS:
			global NUMBER_OF_BALLS
			#checking if there is a collision between the player to a bot
			if collide(i,MY_BALL):
				coludedBallR = i.r
				if i.r > MY_BALL.r:
					lose()

					return False
				elif i.r<= MY_BALL.r:
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
					MY_BALL.r += i.r/3

					i.ht()
					BALLS.remove(i)	
					spawn()
					MY_BALL.shapesize(MY_BALL.r/10)
					getscreen().update()


		return True
	timeWrite = clone()
	timeWrite.pu()
	timeWrite.goto(-SCREEN_WIDTH + 100, SCREEN_HEIGHT - 70)
	def timerDisplay():
		global timeScore
		timeWrite.clear()
		timeWrite.color("red")
		timeWrite.fillcolor("red")
		timeWrite.pu()
		
		timeWrite.pd()
		timeScore = int(time.clock() * 2)
		timeWrite.write("time: " + str(timeScore), False, "left", ("Purisa", 30, "bold"))
		
	#making the player move by hovering with the mouse function
	def movearound():
		VecSpeed = 100.0
		#getting the position of the mouse and saving it as the new player positions
		old_x = MY_BALL.x
		old_y = MY_BALL.y
		mouse_x = (getcanvas().winfo_pointerx() - SCREEN_WIDTH)
		mouse_y = (-getcanvas().winfo_pointery() + SCREEN_HEIGHT)
		MY_BALL.dvx = MY_BALL.dx*((mouse_x - old_x)/VecSpeed)
		MY_BALL.dvy = MY_BALL.dy*((mouse_y - old_y)/VecSpeed)
		# MY_BALL.dvx = ((mouse_x - old_x)/250.0)
		# MY_BALL.dvy = ((mouse_y - old_y)/250.0)

		print(str(mouse_y))


	def lose():
		timepoint = timeScore
		MY_BALL.ht()
		score.ht()
		score.pu()
		score.goto(0,0)
		
		score.st()
		score.pd()
		score.clear()
		score.write("You lost!",font = ("Garuda",40,"bold") ,align="center")
		score.ht()
		score.pu()
		score.goto(-10,-50)
		score.pencolor("orangered")
		score.color("orangered")
		score.pd()
		score.st()
		score.write("coder: Noam Globerman",font = ("DejaVuSerif",30,"bold") ,align="center")
		score.ht()
		score.pu()
		score.goto(0,-100)
		
		score.pd()
		score.st()
		score.write("inspiration: Dan Wrecker",font = ("DejaVuSerif",25,"bold") ,align="center")
		score.color("mediumaquamarine")
		score.pencolor("mediumaquamarine")
		score.ht()
		score.pu()
		score.goto(-SCREEN_WIDTH + 70 , -SCREEN_HEIGHT )
		score.st()
		score.pd()
		score.write("Score: " + str(points),font = ("Purisa",20,"bold") ,align="center")
		
		time.sleep(5)
		clear()
		score.clear()
		MY_BALL.clear()
		for i in BALLS:
			BALLS.remove(i)
			i.clear()
			i.ht()
		for i in FOOD:
			FOOD.remove(i)
			i.clear()
			i.ht()
		menu()
		
	DECAY = 0.00003
	def decay():
		MY_BALL.r -= DECAY * MY_BALL.r
		MY_BALL.shapesize(MY_BALL.r/10)

	while RUNNING:
		start = time.clock()

		move_all_balls()
		movearound()
		if MY_BALL.r > MINIMUM_BALL_RADIUS:
			decay()
		MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
		if check_myball_collision == False:
			
			RUNNING = False
		check_all_balls_collision()
		check_myball_collision()
		
		getscreen().update()
		time.sleep(0.01)
		if MY_BALL.r >= 150:
			win()
		timerDisplay()
def instructions():
	clearscreen()
	setup(1280,720)
	bgcolor("firebrick")
	writing.ht()
	writing.pu()
	writing.goto(0,20)
	writing.pd()
	writing.pencolor("black")

	writing.write("BAGAR IO", font = ("Purisa", 150,"bold"), align = "center")
	writing.pu()
	writing.goto(0,0)
	writing.pd()
	writing.pencolor("white")

	writing.write("*Goal: reach a certain size without getting eaten", font = ("Purisa", 22,"bold"), align = "center")
	writing.pu()
	writing.goto(0,-50)
	writing.pd()
	writing.write("*move with the mouse", font = ("Purisa", 22,"bold"), align = "center")
	writing.pu()
	writing.goto(0,-100)
	writing.pd()
	writing.write("*watch out from the evil balls, they might be smaller, but they will eat you", font = ("Purisa", 17,"bold"), align = "center")
	writing.pu()
	writing.goto(0,-150)
	writing.pd()
	writing.write("*you can change the background colors, by trying different keys on keyboard", font = ("Purisa", 17,"bold"), align = "center")
	writing.pu()
	writing.goto(0,-200)
	writing.pd()
	writing.write("*to go back to the menu, press '1'", font = ("Purisa", 22,"bold"), align = "center")	
	onkey(menu,"1")
	listen()
def menu():
	setup(1280,720)
	clearscreen()
	ht()
	bgcolor("firebrick")
	writing.clear()

	time.sleep(0.5)
	writing.ht()
	writing.pu()
	writing.goto(0,40)
	writing.pd()
	writing.pencolor("black")

	writing.write("BAGAR IO",font = ("Purisa",150,"bold"), align = "center")
	time.sleep(0.5)
	writing.pu()
	writing.goto(0,10)
	writing.pd()
	writing.pencolor("white")

	writing.write("start game(1)", font = ("Purisa", 30,"bold"), align = "center")
	time.sleep(0.5)
	writing.pu()
	writing.goto(0,-50)
	writing.pd()
	writing.write("instructions(2)", font = ("Purisa", 30,"bold"), align = "center")
	time.sleep(0.5)
	writing.pu()
	writing.goto(0,-110)
	writing.pd()
	writing.write("quit(3)", font = ("Purisa", 30,"bold"), align = "center")
>>>>>>> c1ebf657dbac09d837697ce39e43092545610bce:project/agario.py

	onkey(main,"1")
	onkey(instructions, "2")
	onkey(quit,"3")
	listen()
	time.sleep(3)
	clear()

menu()
mainloop()
