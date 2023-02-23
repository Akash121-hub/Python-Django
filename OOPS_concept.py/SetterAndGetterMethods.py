# Setter And Getter methods are ways to achieve the data Encapsulation


class Student:
    def __init__(self,marks,name):
        self.marks = marks
        self.name = name

     # this will update the different instance methods
    @property
    def msg(self):
        return "Hey"+ self.name + " " + " got" + "  "+self.marks

    @msg.setter
    def msg(self,msg):
        sent = msg.split(" ")
        print(sent)
        self.name = sent[0]
        self.marks = sent[-1]
