#Practice with arrays!

#define an array by setting list of elements equal to a variable
x = [0.0, 3.0, 5.0, 2.5, 3.7]	
print("x is a ", type(x))
print("x = ", x)

#remove the third element, recall array elements start with 0
x.pop(2)		#literally pops the 3nd element off the array XD
print("Removed 5.0: ", x)

#remove the element equal to 2.5
x.remove(2.5)	#use instead of pop if using value of element rather than element itself
print("Removed 2.5: ", x)

#add an element at the end
x.append(1.2)
print("Adding 1.2: ", x)

#get a copy
y = x.copy()			#if just set y = x, would be using pointers, could edit original file
print("y = ", y)				#using copy makes a deep copy in memory instead, changes in y dont affect x

#how many elements are equal to 0.0, should be 1
print("Number of zeroes: ", y.count(0.0))	

#print the index with value 3.7
print("3.7 is located in element # ", y.index(3.7))

#sort the list
y.sort()
print("Least to greatest: ", y)

#reverse sort
y.reverse()
print("Greatest to least: ", y)

#remove all elements
y.clear()		#Clears memory of values stored in array
print("Empty y = ", y)
print("X lives! = ", x)
