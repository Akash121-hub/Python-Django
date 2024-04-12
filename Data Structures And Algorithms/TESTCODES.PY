# arr = [2,3,1,4,5,0,6,7,8]
# target = 15
# results = []
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             results.append((arr[i],arr[j]))

# print(results)

# a = "Akash"
# b = "as"

# if b in a:
#     print(True)
# else:
#     print(False)
# even_sqrs = []
# ab =  [even_sqrs.append([i*i,i]) for i in range(100) if i %2 == 0 ]
# print(even_sqrs)

from typing import Counter


frequent_val = "akash"
half_str = len(frequent_val) // 2 
print(frequent_val[:half_str] + frequent_val[half_str:][::-1])
# print(frequent_val[half_str:])
dictionary = Counter(frequent_val.lower())
# print(dictionary)