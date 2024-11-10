# Defining greet function
def greet(name):
	return f"Hello, {name}!"

# Lamda function for addition 
add= lambda x,y: x+y 

list_old = [1,2,3,4]
new_list = [value*2 for value in list_old]
print(new_list)

new_tuple = ("apple", "banana", "orange")
print(new_tuple)
list_new_words = [ "apple", "banana", "apple", "cherry", "banana", "apple"]
from collections import Counter
result = Counter(list_new_words)
print(result.most_common())