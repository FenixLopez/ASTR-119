import numpy as numpy
import sys   #defines all of the command arguments we use

#define a function that returns a value
def expo(x):			
	return np.exp(x)  #return the np e^x function

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call the expo function

#define a main function
def main():
	n = 10   #provide a default value for n

	#check if there is a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])  #if an argument was provided, use it for n

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