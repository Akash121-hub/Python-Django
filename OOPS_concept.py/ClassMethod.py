# if you want to change the class then @classmethod decorator is used
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

c = Student(90,"Akash")
d = Student(99,"Suraj")
print(c.object_count())


        