import numpy as np
import sys
def print_my_name(name):
	#sys.stdout.write(name)
	print name

listOfArguments = sys.argv[1:]
Name = str(listOfArguments[0])

sys.stdout.write(print_my_name(Name))
