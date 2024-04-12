'''Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space. The process by which Python periodically frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.'''

str1 = "KASH"
str2 = ""
# def str1(str):
#     return str1(str[1:]+str[0])

# print(str1("AKASH"))

for i in str1:
    # print(i)
    str2 = i + str2

print(str2)