# arrange list in incrementing order or decrementing order
arr = [2,3,1]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

print(arr)

str1 = "1kash"

str2 = str1[0].isdigit()

print(str2)


def frequent_char(string):
    char_count_dict = {}
    for i in string:
        if i in char_count_dict:
            char_count_dict[i] += 1
        else:
            char_count_dict[i] = 1
    max_count = max(char_count_dict.values())
    char = [char for char,count in char_count_dict.items() if max_count == count]
    print(char,max_count)
    return char_count_dict

print(frequent_char("aabbccdddeeee"))



def reverse(lst,l,r):
    if l >= r:
        return lst
    temp = lst[l]
    lst[l] = lst[r]
    lst[r] = temp

    return reverse(lst,l+1,r-1)

my_lst = [10,9,8,7]

l = 0
r = len(my_lst) - 1

print(reverse(my_lst,l,r))



# Sure, here's a Python program to generate the first 20 prime numbers:

# python
# Copy code
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

count = 0
number = 2
print("First 20 prime numbers:")
while count < 20:
    if is_prime(number):
        print(number, end=" ")
        count += 1
    number += 1