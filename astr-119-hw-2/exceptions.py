#python exceptions let you deal with
#unexpected results
#without the program completely dying on you

try:
	print(a) #this will throw an exception since a is not a previously defined variable
except:
	print("a is not defined!")	#will print this instead of quiting program

#there are specific errors to help with cases
#helps determine what the exact error is
try:
	print(a) #this will throw an exeption since a is not defined
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.") 

#this will break our program
#since a is not defined
print(a)  #no exception to stop the program from breaking completely				