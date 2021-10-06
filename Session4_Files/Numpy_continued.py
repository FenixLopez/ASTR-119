#Using numpy continued
import numpy as np

x = 1.0
y = 2.0

#exponents and logarithm
print(np.exp(x))		#e^x
print(np.log(x))		#ln x
print(np.log10(x))		#log_10 x
print(np.log2(x))		#log_2 x (can set to any base)

#min/max/misc
print(np.fabs(x))		#absolute value as a float - makes positive
print(np.fmin(x,y))		#min of x and y
print(np.fmax(x,y))		#max of x and y

#populate arrays
n = 100					#define an int
z = np.arange(n, dtype=float)	#get an array (0.0 to n-1)
z *= 2.0*np.pi / float(n-1)		#The range of this array is now z = (0, 2*pi)
sin_z = np.sin(z)				#get an array of sinz, can do an operation for all elements without looping!

#interpolation
print(np.interp(0.75,z,sin_z))	#interpolate sin(0.75) - approximate the value?
print(np.sin(0.75))
