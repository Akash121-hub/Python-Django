# Sort array using Bubble sort method in python

arr = [6,5,7,8,3,2,1,4]
size = len(arr) 

for i in range(size):
    for j in range(size-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)