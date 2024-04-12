# MAP :-- These functions can take any other function as a parameter and can be supplied to other functions as parameters as well.

# this function takes another function as a parameter along with a sequence of iterables and returns an output after applying the function to each iterable present in the sequence. Its syntax is as follows:

# SYNTAX:

# map(function, iterables)  

def map_func(a):
    return a*a

res = map(map_func,(2,3,4))
# print(list(res),"......")
# print(res)
# print(tuple(res)) # We can use the set or list or tuple to print the object


# Lambda functions within map():
# Lambda functions are functions that do have any name. These functions are often supplied as parameters to other functions. Now let us try to embed lambda functions within the map() function. Consider the following example:

# EXAMPLE:

tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
newtuple = tuple(map(lambda x: x+3 , tup)) 
print(newtuple)


# The filter() function:
# The filter() function is used to create an output list consisting of values for which the function returns true. The syntax of it is as follows:


# Just like map(), this function can be used can also take user-defined functions as well as lambda functions as a parameter.

# SYNTAX:

# filter(function, iterables)

def func(x):
    if x>=3:
        return x
y = filter(func, (1,2,3,4))  
print(y)
print(list(y))


# Using lambda within filter():

# The lambda function that is used as a parameter actually defines the condition that is to be checked. For example:

# EXAMPLE:

y = filter(lambda x: (x>=3), (1,2,3,4))
print(list(y))


# The reduce() function:
# The reduce() function, as the name describes, applies a given function to the iterables and returns a single value.

# SYNTAX:

# reduce(function, iterables)


from functools import reduce
res = reduce(lambda a,b: a+b,[4+4+4+4+4])


# def mul(a,b,c):
#     return reduce(lambda a,b,c: a*b*c,[a,b,c])

# res = mul(1,2,3)
print(res)

