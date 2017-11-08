class Animal(object):
	def __init__(self, sound, name, age, favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self, food):
		print("Yummy!! " + self.name + " is eating "+  food)
	def description(self):
		print(self.name + " is "+ self.age + " years old and loves the color "+self.favorite_color)
	def make_sound(self):
		print("enter the amount of times you want the animal to make her noise:")
		times = input()
		times = int(times)
		for i in range(times):
			print(self.sound)
animal1 = Animal("coin", "rexi", "15", "blue")
animal1.eat("choclate cake")
animal1.description()
animal1.make_sound()