# StaticMethod

# @staticmethod is a decorator which implements in same way as classmethods
# It won't take take any class or self as a parameter
class Student:
    counter = 0
    def __init__(self,marks,name):
        self.marks = marks
        self.name = name
        Student.counter = Student.counter + 1
    def msg(self):
        print("Hey"+ self.name + " " + " got" + "  "+self.marks)

    @classmethod
    def object_count(cls):
        return cls.counter

    @staticmethod
    def get_age(age):
        if age>29:
            print("They r graduated")
        else:
            print("They are in college or school")

c = Student(90,"Akash")
d = Student(99,"Suraj")
c.get_age(10)