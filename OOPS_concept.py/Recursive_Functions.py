# Recursion is the process of defining something in terms of itself.

# A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 4
print("The factorial of", num, "is", factorial(num))