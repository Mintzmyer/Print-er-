# ##################################
# 
# This is an exercise in modifying python code at runtime, but
# removes the complexity of Blender.
# 
# It explores both of Blender's suggested approaches listed here:
# https://docs.blender.org/api/2.79/info_tips_and_tricks.html
# 
# This script helps examine the functionality and limitations of
# scripts - what date can be passed to and from, what data can
# be stored or lost, what data will be static or refreshed
# 
# ##################################

name = "myScript"
ver = "Version 1.0"
fibNums = [0, 1]

def classData(oldClass):
	global fibNums, name, ver
	name = oldClass.name
	ver = oldClass.ver
	fibNums = oldClass.fibNums

def getFibNums():
	return fibNums

def setFibNums(newFibs):
	global fibNums
	fibNums = newFibs

def sayHi():
	global name, ver
	print("Hello from " + name + ", an excellent script for modifying at runtime.")
	print("This is " + ver + " and can be revved when changed.")

def fib(x):
	global fibNums
	i = 0
	while (i < x):
		try:
			print(fibNums[i])
			i = i+1
		except:
			print("Hmm, let me think...")
			nextFib = fibNums[i-1] + fibNums[i-2]
			fibNums = fibNums + [nextFib]

sayHi()
setFibNums(sys.argv)
fib(5)
fib(7)