# There are 3 Basic built in decorators
# 1. Property
# 2. Classmethod
# 3. StaticMethod

############### property decorator ###############

# 1. it will allow us to call class method as an attribute
# 2. we can replace setter and getter method by using property decorator
class Student:
    def __init__(self,marks,name):
        self.marks = marks
        self.name = name

    @property # this will update the different instance methods
    def msg(self):
        return "Hey"+ self.name + " " + " got" + "  "+self.marks

obj = Student("90", "Akash")

print(obj.msg)







class Student:
    def __init__(self,marks,subject):
        self.marks = marks
        self.subject = subject
    
    # @property
    def msg(self):
        print("hey"+ " in  " + self.subject+ " " + "you got " + self.marks)

c = Student("90","science")
c.msg
        