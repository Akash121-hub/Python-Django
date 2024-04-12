# Opertaions to perform

ex_dictionary = {'name':'Akash', 'Id':200, 'Salary':9080}

d = {}

d.update(ex_dictionary)  # update the dictionary into the other dictionary

print(len(ex_dictionary),ex_dictionary) # LENGTH OF DICTIONARY

ex_dictionary['name'] = 'Suraj' # Replacing the value of key name


def func(dictionary): # via function check the key is present or not
    dictionary = {'name':'Akash', 'Id':200, 'Salary':9080}

    if 'Gender' in dictionary:
        return True
    else:
        return False

sa = func({'name':'Akash', 'Id':200, 'Salary':9080})


# Write a prgm to create a dict with player names and runs in a match. Alaso retrive the runs by entring the entring player's name

'''x = {}

print("how many players ??  ")

n = int(input())

for i in range(n):
    print("enter player name:  ")
    k = input()
    print("enter score")
    v = int(input())
    x.update({k:v})


name = input()

runs = x.get(name,-1)

if runs == -1:
    print("Player not found")
else:
    print("runs made by player {},  {}  ".format(name,runs)) '''



dict = {}

str = "Easebuzz"

count = 0
for x in str:
    dict[x] = dict.get(x,0) + 1


colors = {100:'red', 200:'green', 50:'yellow', 800:'pink'}

sorted_dict_by_keys = sorted(colors.items(), key=lambda y:y[0]) # Sorting of dictionary by KEYS

sorted_dict_by_values = sorted(colors.items(), key=lambda y:y[1]) # Sorting of dictionary by VALUES

 