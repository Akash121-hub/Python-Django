# Setter And Getter methods are ways to achieve the data Encapsulation


# class Student:
#     def __init__(self,marks,name):
#         self.marks = marks
#         self.name = name

#      # this will update the different instance methods
#     @property
#     def msg(self):
#         print( "Hey"+ self.name + " " + " got" + "  "+self.marks )

#     @msg.setter
#     def msg(self,msg):
#         sent = msg.split(" ")
#         print(sent)
#         self.name = sent[0]
#         self.marks = sent[-1]
    
# obj = Student.msg
# print(obj)

class Developer:
    def __init__(self,age,Name,companyName,salary):
        self.age = age
        # self.name = name
        self.Name = Name
        self.companyName = companyName
        self.salary = salary
    @property
    def company(self):
        return self.companyName

    @company.setter
    def company(self,companyName):
        self.companyName = companyName

developer = Developer(22,"akash","tata technologies",100000)
print(developer.company)



