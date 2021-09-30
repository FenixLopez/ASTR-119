import numpy as np  #we use numpy for lots of things

def main():
	i = 0     #integers can be declared with a number
	n = 10	  #here is another integer
	x = 119.0 #floating point numbs are declared with a "." determine sigfig later

	# we can use numpy to declare arrays quickly

	y = np.zeroes(n, dtype=float)  #delcared 10 zeroes as floats using array np

	# we can use for loops to iterate with a variable

	for i in range(n):  #makes a "for loop" for i in range (o, n-1) #goes 0 to 9
		y[i] = 2.0 * float(i) +1. #set y = 2i+1 as floats

		#we can also simpply iterate through a variable
		for y_element in y:
			print(y_element)   #looping through every element in y and printing in sequence

#execute the main function
if __name__ == "__main__":
	main()
 