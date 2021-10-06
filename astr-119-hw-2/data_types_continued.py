#Continuing to try different data types

#string

s = "I am a string."		
print("'I am a string is a' is a ", type(s))			#will say str

#Boolean

yes = True				#Boolean True
print(type(yes))

no = False				#Boolean False (these are protected terms in python)
print(type(no))

#List -- ordered and changeable list of variables, using []
#wish C++ was this nice about arrays :V

alpha_list = ["a", "b", "c"]	#List initialization with strings
print("alpha_list is a ", type(alpha_list))	#will say tuple
print("an array of ", type(alpha_list[0]))		#will say string
alpha_list.append("d")			#will add "d" to the list end
print("new list: ", alpha_list)					#will print list

#Tuple - ordered and unchangeable, using ()
alpha_tuple = ("a", "b", "c")  #tuple initialization
print("alpha_tuple is a ", type(alpha_tuple))	#will say tuple

try:							#attempt the following
	alpha_tuple[2] = "d"		#wont work and will raise TypeError
except TypeError:				#when we get a TypeError
	print("We can't add elements to tuples!") #print this message
print("same alpha_tuple: ", alpha_tuple)		#will print tuple	


#class is a type of data, contains elements and member functions, a
#list has member functions and therefore a type of class
#everything we define will be a class 

#try - Python is great at checking you and seeing it code words
#explicitly tells you where the bugs are