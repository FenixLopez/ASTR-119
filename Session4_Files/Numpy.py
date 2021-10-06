import numpy as np 

x = 1.0		#define a float
y = 2.0		#define another float

#trigonometry
print(np.sin(x))		#sin(x)
print(np.cos(x))		#cos(x)
print(np.tan(x))		#tan(x)
print(np.arcsin(x))		#arcsin(x)
print(np.arccos(x))		#arccos(x)
print(np.arctan(x))		#arctan(x)
print(np.arctan2(x,y))	#arctan(x/y)  #takes 2 elements and does x/y
print(np.rad2deg(x))	#convert radians to degrees

#hyperbolic functions - QM - linear combinations of e^x and e^-x
print(np.sinh(x))		#sinh(x)
print(np.cosh(x))		#cosh(x)
print(np.tanh(x))		#tanh(x)
print(np.arcsinh(x))	#arcsinh(x)
print(np.arccosh(x))	#arccosh(x)
print(np.arctanh(x))	#arctanh(x)