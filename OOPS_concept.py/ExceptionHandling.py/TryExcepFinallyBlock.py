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

# use of finally block
# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.
def func(nums):
# try block
    try:
        a = int(input("Enter numerator number: "))
        b = int(input("Enter denominator number: "))
        print("Result of Division: " + str(a/b))
    # except block handling division by zero
    except(ZeroDivisionError):
        print("You have divided a number by zero, which is not allowed.")
        return None
    finally:
        print("Code execution Wrap up!")
func([1,23])
# outside the try-except block
print("Will this get printed?")
"""
It makes a difference if you return early:

try:
    run_code1()
except TypeError:
    run_code2()
    return None   # The finally block is run before the method returns
finally:
    other_code()
Compare to this:

try:
    run_code1()
except TypeError:
    run_code2()
    return None   

other_code()  # This doesn't get run if there's an exception.

"""