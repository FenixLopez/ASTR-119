# This is an example of the If- Else statement

#define a function
def flow_control(k):  #basically controlling information presented depending on circumstances given

	#define a string based on the value of k sent into the function
	if(k==0):
		s = "Variable k = %d equals 0." % k  #takes value of k and places in place of %d

	elif(k==1):
		s = "Variable k = %d equals 1." % k

	else:
		s = "Variable k = %d does not equal 0 or 1." % k

	#print the variable
	print(s)

#define a main function
def main():
	
	#delcare an integer
	i = 0
	flow_control(i)
	# try flow_control for 1 and 2 as well
	# setting to different values to see all parts of if-else statement
	
	i = 1
	flow_control(i)
	
	i = 2
	flow_control(i)

#run the program, call main 
if __name__ == "__main__":
	main()
