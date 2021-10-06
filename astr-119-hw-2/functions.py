import numpy as np
import sys   #defines all of the command arguments we use

#define a function that returns a value
#returns one variable
def expo(x):			
	return np.exp(x)  #return the np e^x function

#define a subroutine that does not return a value - void function in C++!
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call the expo function
		#this prints the elements in array after exponent operation

#define a main function
def main():
	n = 10   #provide a default value for n

	#check if there is a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])  #if an argument was provided, use it for n
		#by typing number in command line, can affect the number of iterations
		#ex: if type 3 after "python3 functions.py", will show only 3 floats
		#if not given a value, will default to 10

	show_expo(n)	#calls the show_expo subroutine to print values

#run the main function
if __name__ == "__main__":    #must call main program
	main()

'''
when creaing functions in python with python3, 
terminal will check if we are at the highest level of program via
the protected __name__

python will not execute functions unless
specifically called.
'''