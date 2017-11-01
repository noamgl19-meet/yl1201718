# print("write your name: ")
# name = input()
# i = 1
# while i<=100:

# 	print("your name is "+ name)
# 	i +=1

# number1 = input()
# number2 = int(number1)/2
# print(number2)
list = [1,3,5]
number = 0
for i in list:
	print(i)
	number +=i
print(number)
# for i in list:
# 	print(i*2)
import turtle
turtle.pensize(10)
turtle.shape("square")
turtle.ht()
turtle.pu()
turtle.goto(-200,70)
turtle.pd()
turtle.color("blue")
# turtle.begin_fill()
# turtle.goto(0,100)
# turtle.goto(100,100)
# turtle.goto(100,0)
# turtle.goto(0,0)
turtle.circle(100)
turtle.end_fill()
#
turtle.pu()
turtle.goto(0,70)
turtle.pd()
turtle.color("black")
turtle.circle(100)
turtle.end_fill()
#
turtle.pu()
turtle.goto(200,70)
turtle.pd()
turtle.color("red")
turtle.circle(100)
turtle.end_fill()
#bottom
turtle.pu()
turtle.goto(-100,-70)
turtle.pd()
turtle.color("yellow")
turtle.circle(100)
turtle.end_fill()
#
turtle.pu()
turtle.goto(100,-70)
turtle.pd()
turtle.color("green")
turtle.circle(100)
turtle.end_fill()

turtle.mainloop()
