#define a dictionary data structure

#dictionaries have key : value for the elements
#associates a key with value
#can associate two different types of data together
#think - you are looking up the definition of a word
example_dict = {
	"class:"			:	"Astr 119",
	"prof:"			:	"Brant",
	"awesomeness:"	:	10
}
print("example_dict is a ", type(example_dict)) #will say dict
print("Original dictionary:")		#print original dictionary before editing values
print(example_dict)

#get a value via key
#think - definition of a specific word in dictionary
course = example_dict["class:"]
print("Class: ", course)

#change a value via key
#will change the corresponding definition of the key
example_dict["awesomeness:"] += 1 #increase awesomeness

#print the updated dictionary
print("Updated dictionary:")
print(example_dict)

#print dictionaray element by element
print("Dictionary element by element:")
for x in example_dict.keys():
	print(x, example_dict[x])
