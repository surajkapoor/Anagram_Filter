import random
import json


class Create_List(object):

	def __init__(self):
		self.pre_ordered_list = []
		
	def create_file(self):
		choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
		while len(self.pre_ordered_list) < 1000:
			c = random.sample(choices, 3)
			self.pre_ordered_list.append([''.join(c)])
		with open("anagram_list.txt", "w") as f:
			json.dump(self.pre_ordered_list, f)
		return	


c = Create_List()
c.create_file()		