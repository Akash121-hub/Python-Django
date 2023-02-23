# Two Types of Time complexity and Space Complexity

from numbers import Complex


# Time Complexity : The no of times statements executed

# Types : 1. Theoritical 2. Experimental

# 1. Experimental --> Depends upon the OS that you are using, No of process runnign parallely, no inputs given, RAM, 

import time
start = time.time()
arr = [1,2,3,4,5,2,1]
found = -1

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            found = arr[i]
            arr.remove(found)

print(found)

end = time.time()

print(1000*(end-start))

print(arr)

# Theoritical Analysis

arr1 = [2,3,45,3,5,6,7,2] # K1 Work -- CONSTANT
found1 = -1 # K2 Work -- CONSTANT

for i in range(0,len(arr1)): # n times arrat is going to run (len(arr)) times
    for j in range(i+1,len(arr1)): # n times
        if arr1[i] == arr[j]: # K3 work we are comparing ( Constant )
            found1 = arr1[i] # K4 work

print(arr1) # K5 Work

"""
In above example k1+k2+K*n*n + k5 == c + k*n^2 <= (k+1) n & 2
"""


# Examples to calculate time complexity

# Example 1
print("Hello World") # --> O(c) --> drop the constant which is c --> O(1) the Order of 1.

# Example 2
print("Hello Akash") # c1 --> constant 
print("Hello You there") # c2 --> constant
print("Hello you have got the job") # c3 --> constant

# Example 3 

n = 10 # c1 --> constant
for i in range(n): #--> c2
    print("Hey Akash") # --> n*c3
## c1+c2+(n*c3) --> n * c3 --> O(c3)

# Example 4
x = 10
y = 20

for i in range(x): # c1
    print("Hey") #c2*x
    for j in range(y): #c3 * x
        print("Hey i love python") #c4*x*y

# tc = c1 + x*c2 + x*c3 + c4*n*m --> keep the highest values and neglect other values --> O(x*y)

