import random
list1 = [0,1,2,3]
list2 = []
class Songs(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for i in range(len(self.lyrics)):
			z = random.choice(range(4))
			for i in list2:
				if z in list2:
					z = random.choice(range(4))
				
					list2.append(z)

			print(self.lyrics[z])

song = Songs(["roses are red", "that much is true.", "But violets are purple", "not freaking blue."])
song2 = Songs(["i wanna be a ", "minority", "I don't need your", "authority"])
list = [song,song2]

random.choice(list).sing_me_a_song()
random.choice(list).sing_me_a_song()


