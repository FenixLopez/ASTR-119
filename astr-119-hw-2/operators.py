# Utilizing multiple python operators

# Initializing some variables
x = 9
y = 3

# Arithmetic Operators - several math functions
# You can write the operation within print and it will print the answer
print("9 + 3 = ", x+y) 		# Addition
print("9 - 3 = ", x-y)		#Subtraction
print("9 * 3 = ", x*y)		#Multiplication
print("9 / 3 = ", x/y)		#Division
print("9 ^ 3 = ", x**y)		#Exponentiation

# Setting x to a floating point to use modulus and floor division
x = 9.191923

# Arithmetic Operators continued
print("9.191923 % 3 = ", x%y)
print("9.191923 // y = ", x//y)

# Assignment Operators 
x = 9		# set x = 9 again 
x += 3      # x = x + 3
print("9 + 3 = ", x)
x = 9
x -= 3      # x = x - 3
print("9 - 3 = ", x)
x *= 3      # x = x * 3
print("6 * 3 = ", x)
x /= 3      # x = x / 3
print("18 / 3 = ", x)
x **= 3      # x = x ^ 3
print("6 ^ 3 = ", x)

#Comparison Operators
x = 9
y = 3
print("Does 9 == 3? ", x==y)     #True if x equals y, false otherwise
print("Does 9 != 3? ", x!=y)	 #True if x does not equal y, false otherwise
print("Is 9 > 3? ", x>y)		 #True if x greater than y, false otherwise
print("Is 9 < 3? ", x<y)   		 #True if x less than y, false otherwise
print("Is 9 >= 3? ", x>=y) 	 	 #True if x is greater than or equal to y, false otherwise
print("Is 9 <= 3? ", x<=y)		 #True if x is less than or equal to y, false otherwise