# Python Generators are the capabilities that return the crossing object and used to make iterators. It simultaneously traverses all of the items. The generator can also be an expression with syntax similar to that of Python's list comprehension.

"""
Advantages of Generators
There are various advantages of Generators. Few of them are given below:

1. Easy to implement
Generators are easy to implement as compared to the iterator. In iterator, we have to implement __iter__() and __next__() function.


2. Memory efficient
For many sequences, generators utilize memory efficiently. The generator function, on the other hand, calculates the value and suspends their execution, whereas the normal function returns a sequence from the list, which first creates the entire sequence in memory before returning the result. It resumes for progressive call. A limitless succession generator is an extraordinary illustration of memory streamlining. Let's talk about it using the sys.getsizeof() function in the example below


3. Pipelining with Generators
Information Pipeline gives the office to handle huge datasets or stream of information without utilizing additional PC memory.

Let's say we have a famous restaurant's log file. The log document has a section (fourth segment) that monitors the quantity of burgers sold consistently and we need to total it to find the complete number of burgers sold in 4 years. The generator can create a pipeline using a series of operations in that scenario. The code for it is as follows:

with open('sells.log') as file:  
burger_col = (line[3] for line in file)  per_hour = (int(x) for x in burger_col if x != 'N/A')  
print("Total burgers sold = ",sum(per_hour))  
4. Generate Infinite Sequence
The generator can produce infinite items. Infinite sequences cannot be contained within the memory and since generators produce only one item at a time, consider the following example:

def infinite_sequence():  
    num = 0  
    while True:  
        yield num  
            num += 1  
  
for i in infinite_sequence():  
    print(i)  
"""


def test_generator(nums):
    for i in range(len(nums)):
        yield i
abc = [1,3,4,5]
instan = test_generator(abc)

print(instan.__next__())
print(instan.__next__())
print(instan.__next__())
print(instan.__next__())
print(instan.__next__())

# Example: Write a program to print the table of the given number using the generator.

def table(n):
    for i in range(1,11):
        yield n*i
        i += 1

for i in table(15):
    print(i)

import sys  
# List comprehension  
nums_squared_list = [i * 2 for i in range(100)]  
print(sys.getsizeof("Memory in Bytes:",nums_squared_list))  
# Generator Expression  
nums_squared_gc = (i ** 2 for i in range(100))  
print("//",sys.getsizeof("Memory in Bytes:", nums_squared_gc))  

