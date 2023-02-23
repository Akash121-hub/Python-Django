# ListComprehension -->  List comprehensions are used for creating new lists from other iterables like tuples, strings, arrays, lists, etc. A list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element. 
 
# SYNTAX :

    # newList = [ expression(element) for element in oldList if condition ] 

# Advantages: 

# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula

            # EXAMPLE
# Empty list
List = []
 
# Traditional approach of iterating
for character in 'Geeks 4 Geeks!':
    List.append(character)
 
# Display list
print(List)


# Using list comprehension to iterate through loop
List = [character for character in 'Geeks 4 Geeks!']
 
# Displaying list
print(len(List))

# using lambda to print table of 10
numbers = list(map(lambda i: i*10, [i for i in range(1,6)]))
 
print(numbers)







even =  [i for i in range(1,100) if (i % 2) == 0]
print(even)