class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
    def display(self):
        print(self.name,self.age)
emp=Employee("deeskah",55)
emp1=Employee("Raksha",66)
emp.display()
emp1.display()
