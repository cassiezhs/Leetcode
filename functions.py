'''enumerate() is a built-in function that allows you to loop through an iterable (like a list, tuple, 
or string) while keeping track of both the index and the value of each item. 
It adds an automatic counter (starting at 0 by default) to the items in the iterable.
enumerate(iterable, start=0)
iterable: The object you want to loop through.
start (optional): The starting value of the counter. Defaults to 0.
'''
# Basic Usage
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits):
    print(index, value)

# Starting the Index at a Different Value
fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits, start=1):
    print(index, value)

# Starting the Index at a Different Value
fruits = ['apple', 'banana', 'cherry']
result = list(enumerate(fruits))
print(result)