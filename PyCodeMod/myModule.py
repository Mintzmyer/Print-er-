# ##################################
# 
# This is an exercise in modifying python code at runtime, but
# removes the complexity of Blender.
# 
# It explores both of Blender's suggested approaches listed here:
# https://docs.blender.org/api/2.79/info_tips_and_tricks.html
# 
# This module helps examine the functionality and limitations of
# modules - what date can be passed to and from, what data can
# be stored or lost, what data will be static or refreshed
# 
# ##################################

def fib(fibArray, x):
	i = 0
	while (i < x):
		try:
			print(fibArray[i])
			i = i+1
		except:
			print("Hmm, this array needs another fibonacci number...")
			nextFib = fibArray[i-1] + fibArray[i-2]
			fibArray = fibArray + [nextFib]
	return fibArray

class myClass:
	name = "myModule"
	ver = "Version 1.0"
	fibNums = [0, 1]

	def update(self, oldClass):
		self.name = oldClass.name
		self.ver = oldClass.ver
		self.fibNums = oldClass.fibNums

	def sayHi(self):
		print("Hello from " + self.name + ", an excellent module for modifying at runtime.")
		print("This is " + self.ver + " and can be revved when changed.")

	def fib(self, x):
		i = 0
		while (i < x):
			try:
				print(self.fibNums[i])
				i = i+1
			except:
				print("Hmm, let me think...")
				nextFib = self.fibNums[i-1] + self.fibNums[i-2]
				self.fibNums = self.fibNums + [nextFib]