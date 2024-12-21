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

import re
sentence = "Hello    World   Python"
print(re.sub(' +', ' ', sentence))  # Output: "Hello World Python"

#reversing
nums = (1, 2, 3, 4)
reversed_nums = nums[::-1]
print(reversed_nums)  # Output: (4, 3, 2, 1)

words = ["apple", "banana", "cherry"]
reversed_words = words[::-1]
print(reversed_words)  # Output: ['cherry', 'banana', 'apple']

#join
words = ['Hello', 'World']
print(" ".join(words))  # Output: "Hello World"

#split
s = "Hello World! Welcome to Python."
result = s.split()
print(result)  # Output: ['Hello', 'World!', 'Welcome', 'to', 'Python.']