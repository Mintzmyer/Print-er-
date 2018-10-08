# ##################################
# This is an exercise in exploring 
# 
# 
# 
# ##################################


import sys
import os
import time

mod_dir = os.path.dirname("~/Print-er-/PyCodeMod")
if mod_dir not in sys.path:
   sys.path.append(mod_dir)

import myModule
import importlib

print(mod_dir)
myScript = "/Users/<Username>/Print-er-/PyCodeMod/myScript.py"

def run(script, args):
	sys.argv = args
	exec(compile(open(script).read(), script, 'exec'))

oldClass = myModule.myClass()
newClass = myModule.myClass()

fibArr = [0, 1]

while(1):
	importlib.reload(myModule)
	prevClass = newClass
	newClass = myModule.myClass()
	newClass.update(prevClass)

	print("New myClass class:")
	newClass.sayHi()
	newClass.fib(4)
	print("Module function:")
	fibArr = myModule.fib(fibArr, 4)
	print("Executing Script:")
	run(myScript, newClass.fibNums)
	print("-------------------- --------------------")
	time.sleep(10)