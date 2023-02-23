                # Break statement
# The break statement is used to terminate the loop or statement in which it is present.

    
s = 'gseeksforgeeks'
# Using for loop 
for letter in s: 
    
    print(letter) 
    # break the loop as soon it sees 'e' 
    # or 's' 
    if letter == 'e' or letter == 's': 
        break
    
# print("Out of for loop") 
# print() 
    
i = 0
    
# Using while loop 
while True: 
    print(s[i]) 
    
    # break the loop as soon it sees 'e' 
    # or 's' 
    if s[i] == 'e' or s[i] == 's': 
        break
    i += 1
    
print("Out of while loop", i)



                    # Continue statement
# Continue is also a loop control statement just like the break statement. continue statement is opposite to that of break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.

# loop from 1 to 10 
for i in range(1, 11): 
    
    # If i is equals to 6,   
    # continue to next iteration   
    # without printing  
    if i == 6: 
        continue
    else: 
        # otherwise print the value 
        # of i 
        print(i, end = " ")

#                 pass Statement
# As the name suggests pass statement simply does nothing. The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute. It is like null operation, as nothing will happen is it is executed.

s = "geeks"
# Pass statement
for i in s:
    if i == 'k':
        print('Pass executed')
        pass
    print(i)