from turtle import *
import time
from agario import main
clear()
ht()
bgcolor("silver")
writing = clone()
writing.clear()

time.sleep(0.5)
writing.ht()
writing.pu()
writing.goto(0,150)
writing.pd()
writing.write("Bagar.io!",font = ("lklug",35,"bold"), align = "center")
time.sleep(0.5)
writing.pu()
writing.goto(0,10)
writing.pd()
writing.write("start game(S/s)", font = ("DejaVuSansMono", 30,"bold"), align = "center")
time.sleep(0.5)
writing.pu()
writing.goto(0,-40)
writing.pd()
writing.write("options(O/o)", font = ("DejaVuSansMono", 30,"bold"), align = "center")
def startGame():
	clear()
	writing.clear()
	main()

onkey(startGame,"S")
onkey(startGame,"s")
listen()








mainloop()