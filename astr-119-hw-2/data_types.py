#we are writing everything in the highest form of the program - global!
# dont need if -> main stuff

#import numpy library, allows us to print data types of variables
import numpy as np  

#declaring integers

i = 10  #integer
print("10 is a ", type(i)) 		#prints out the data type of i

a_i = np.zeros(i, dtype=int) 	#declare an array of ints
print("a_i is a ", type(a_i))	#will return ndarray
print("#bits: ", type(a_i[0]))	#will return int64 - using 64 bits to represent the integer

#declaring floats

x = 119.0  						#floating point number
print("119.0 is a ", type(x))	#print out the data type of x -> floating poitn

y = 1.19e2  					#float 119 in scientific notation
print("1.19e2 is a ", type(y)) 	#print out the data type of y

z = np.zeros(i, dtype=float)  	#declare array of floats
print("z is a ", type(z))		#will return nd array
print("#bits: ", type(z[0]))	#will return float64

b = np.zeros(i, dtype=np.float64)  #can specify the precision of the float, aka amount of memory is can use
print("b is a ", type(z))		#will return nd array
print("b precision is : ", type(z[0]))	#will return numpy.float64
