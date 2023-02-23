#               ARRAYS 
# 1. Can store only one data type of elements 
# 2. More Faster than lists and execution time is less
# 3. Arrays Use less memory than lists
# 4. Can grow and shrink memory dynamically

# Create Array

from array import array


# arrayname = array( typecode, [elements]) 

ex_arr = array('i', [1,2,3,4,5,6,7,8])

# Creating same type of array using another array

arr_2 = array(ex_arr.typecode,(a for a in ex_arr))

# Bubble Sort

sort_arr = array('i', [2,1,4,6,4,5])

size = len(sort_arr)

Sorted = False
for i in range(size-1):
    for j in range(size-1-i):
        if sort_arr[j] > sort_arr[j+1]:
            tmp = sort_arr[j]
            sort_arr[j] = sort_arr[j+1]
            sort_arr[j+1] = tmp
            Sorted = True
    if not sorted:
        break



# Types of Arrays

# Single or One Dimensional array --> These arrays represent only one row or one column of elements

marks = array('i', [50,60,70,66,72])

# Working with arrays using numpy

# The arrays which are created using numpy called n dimensional array

