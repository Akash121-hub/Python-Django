# n Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module. In Python, we can actually change the behavior of code at run-time.
import monk
def monkey_func(self):
    print("This is monk function running")


monk.A.func = monkey_func

obj = monk.A()

obj.func()