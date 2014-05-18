import json

class AnagramSort(object):

	def __init__(self):
		with open("anagram_list.txt") as f:
			self.anagram_list = json.load(f)
		f.close()	
		self.anagram_table = {}

	def add_to_table(self):
		for each in self.anagram_list:
			sorted_string = "".join(sorted(each[0]))
			if sorted_string in self.anagram_table:
				value = self.anagram_table[sorted_string] + ", " + each[0]
				self.anagram_table[sorted_string] = value
			else:
				self.anagram_table[sorted_string] = sorted_string + ", " + each[0]
		return self.anagram_table

	def print_table(self):
		table = self.add_to_table()
		counter = 0
		for each in table:
			print table[each]

if __name__ == "__main__":			
	a = AnagramSort()
	a.print_table()			
