#Importing useful modules 
#These outside programs as added and set equal to local variables
#To be used in this present module

import numpy as np  #the Numpy library
import matplotlib.pyplot as plt	#Matplotlib's pyplot - need to download first

import sys			#gives access to a C-like sys ibrary
import os			#gives access to the operating system

print(sys.argv)		#prints any command line arguments, including program naem
print(os.getcwd()) 	#prints the current working directory