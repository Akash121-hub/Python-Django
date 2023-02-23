'''String = " Hey this is"
result = []
for i in String.split():
        result.append(i)
max_len_word = ""
for i in result:
        if len(i) > len(max_len_word):
                max_len_word = i
                # i = i + 1

print(max_len_word)'''

'''elements = [0,1,2,0,3,0,4,5]

pre_idx = 0

for i in range(len(elements)):
        if elements[i] != 0:
                temp = elements[pre_idx]
                elements[pre_idx] = elements[i]
                elements[i] = temp
                pre_idx += 1
print(elements)'''

# number = 121
# rev_num = 0
# digit = 0

# while (number // 10**digit) != 0:
#         rev_num = (rev_num*10) +((number // 10**digit) % 10)
#         digit += 1

# print(number==rev_num)


# scnd_largest_no 


# arr = [10,7,6,6,5,4,100]

# first_max = max(arr[0], arr[1])
# second_max = min(arr[0], arr[1])
# n = len(arr)

# for i in range(2,n):
#         if arr[i] > first_max:
#                 second_max = first_max
#                 first_max = arr[i]
#         elif arr[i] > second_max and first_max != arr[i]:
#                 second_max = arr[i]

# print(second_max)

# x = 0
# while x < 20:
#         x = x+3
#         print(x)
# print(x)

# def x(values):
#         values[0] = 1
#         return values

# a = x([2,3,4,5])
# print(a)

list1 = ['C++','Java','Python']

if 'java' in list1:
        print(1)
else:
        print(2)


# Preferred time complexities is
# O(1) < O(logn) < O(sqrt(n)) < O(n) < O(nlogn)