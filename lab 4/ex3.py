class Person(object):
	def __init__(self,name,age,gender,city):
		self.name = name
		self.age = age
		self.gender = gender
		self.city = city

	def favorite_breakfast(self, favorite_breakfast):
		self.favorite_breakfast = favorite_breakfast
		print("yum! " + self.name + " has eaten "+ favorite_breakfast)
person = Person("nick", 32, "male", "New yorck")
person.favorite_breakfast("cake!")
