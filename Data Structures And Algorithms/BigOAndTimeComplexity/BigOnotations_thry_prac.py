# BIG O NOTATION : --> :

# Big o notation is used to measure how running time or space requirements for your program grow as input size grows.

# Size of arrays grows time also grows -- > *** Time is Linearly propotional to size of array *** .

        # time = a*n + b

        # Keep fastest growing to terms

        # n is size of the array

# a is time constant
        #   time = a*n ( b is constant )
        #  time = O(n) ( a is constant ) --> Order of n

def get_squared_numbers(numbers):
    squared_numbers = []
    for i in numbers:
        squared_numbers.append(i*i)
    return squared_numbers

numbers = [2,3,4,5,6,7]
print(get_squared_numbers(numbers))

# Find duplicate of numbers in given array
# Linear equation : --> : time = a*n2 + b