class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print(self.name,self.age)
class sample(Employee):
    def __init__(self,marks,rollno):
        self.marks=marks
        self.rollno=rollno
    def  printname1(self):
        print(self.marks,self.rollno)

a=sample(23,77)
a1=Employee("deeksha",33)
a1.printname()
a.printname1()


