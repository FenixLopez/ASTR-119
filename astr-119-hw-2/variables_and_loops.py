import numpy as np 		#many useful functions, manipulation of storage

def main():
	i = 0				# writing a number declares i as an integer
	n = 10				# multiple integers
	x = 119.0 			# "." makes the number a floating point

	# arrays are one of the functions of numpy
	y = np.zeros(n, dtype=float)	#declares 10 zeros (from n) as floats (using dtype) using np

	# Example of a for loop to iterate with a variable
	for i in range(n):	#i iterates in the range [0,n-1]
		y[i] = 2.0 * float(i) +1  # sets y=2i+1 as floats

	# we can iterate through a variable, print each element in array
	for y_element in y:
		print(y_element)

# Execute the main function - need to call it using 
# the protected term __name__ in the highest level of the program
if __name__	== "__main__":
	main()
		