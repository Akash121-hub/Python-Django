# Super method

# super().__init__()

# Calling a parent constructor within a child class executes the operations of the parent class constructor in the child class.

# Python3 program for illustration 
# of values() method in finding total salary
  
  
# stores name and corresponding salaries
salary = {"raj" : 50000, "striver" : 60000, "vikram" : 5000} 
  
# stores the salaries only
list1 = salary.values() 
print(sum(list1))  # prints the sum of all salaries