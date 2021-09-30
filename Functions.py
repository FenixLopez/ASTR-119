import numpy as np
import sys    #allows access to the operating system, pass command line arguments to the script

#define a function that returns a value
def expo(x):
	return np.exp(x)  #return the np e^x function

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) #call the expo function
		#want a floating point version of i instead of an integer, changing type

#define a main function
def main():
	n = 10 #provide a default function for n

	#check if there is a command line argument provided
	if(len(sys.argv)>1):		#what does "len" do??? and .argv???
		n = int(sys.argv[1])  #if an argument was provided, use it for n
								#change n to be the 2nd command line 

	show_expo(n)			#call the show_expo subroutine

#run the main function
if __name__ == "__main__":  #protected variable with double underscores
	main() 



'''
porter-100-64-67-135:ASTR 119 Programs FenixLopez$ python3 Functions.py 4
1.0
2.718281828459045
7.38905609893065
20.085536923187668
'''
#if add a 4 after the name of the function, changes the function