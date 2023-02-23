# Exceptions --> Exception is a runtime error which can be handled by the programmer. that means if he can guess the error in the program and he can do something to eliminate the harm caused by that error. That is called ''exception". 

# Else block and Finally blocks are not compulsory
# When there is no exception, else block is executed after try block
# Finally Block is always executed
# Multiple except blocks can be used to handle multiple exceptions

# EXAPMLE
try:
    pass # statements
except Exception: # 1 exception
    pass 
except Exception: # 2 exception
    pass
except Exception: # 3 exception
    pass
finally:
    pass # statements
