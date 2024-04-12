"""
Classes Are Objects
Let’s see what happens when we call the __class__ attribute on the list class itself, like so:

print(my_list.__class__.__class__)
Output:

<class 'type'>
In the output above, we can see that the list class is an instance of the type class. This is an example of metaclasses at work.

A metaclass is a class that allows for other classes to be instantiated as objects of the metaclass.

In our example, the type class is an example of a metaclass, and the list class is an instance (or object) of the type class.

Here is an example showing that the str and list classes are all instances of the type class:

print("a".__class__)
print("a".__class__.__class__)

print("\n")

print([1].__class__)
print([1].__class__.__class__)
Output:

<class 'str'>
<class 'type'>

<class 'list'>
<class 'type'>
Everything in Python is an instance of a class. If you check the type of the Boolean, function, and floating point types, you will find that they are all instances of a class. Consequently, everything in Python is an object.
class ExampleMetaClass(type):
    pass


class SubClass(metaclass=ExampleMetaClass):
    pass


subclass_object = SubClass()

print(f"subclass_object's class is {subclass_object.__class__}/n")
print(f"SubClass's class is {subclass_object.__class__.__class__}/n")
print(f"ExampleMetaClass's class is {subclass_object.__class__.__class__.__class__}")

"""