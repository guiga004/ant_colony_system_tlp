__author__ = "Rohan Pandit" 

from brute_force import algorithm
import numpy as np
from time import time
from tkinter   import Tk, Canvas
from random import randint

screenSize = 700

def main():
	#loading data
	f = open("datasets/tsp0038.txt", 'r').read().splitlines()
	numCities = f.pop(0)
	cities = np.array([ tuple( map( float, coord.split() ) ) for coord in f ])
	
	#calculating path
	start = time()
	path, length = algorithm( cities )
	print(path)

	tottime = time() - start
	print( "Found path of length %s in %s seconds" % ( round(length,2), round(tottime, 2) ) )

main()
