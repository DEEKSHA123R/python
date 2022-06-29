'''class A:
    def t(self):
        print("parent")
class B:
    def t1(self):
        print("parent1")
class c(A,B):
    def t3(self):
        print("child")


obj=c()
obj.t()
obj.t1()
obj.t3()
print(issubclass(B,A))
print(issubclass(c,B))'''

#method overiding#
'''class Father:
    def transport(self):
        print("bike")
class son(Father):
    def transport(self):
        print("car")

obj1=son()
obj1.father()'''
class p1:
    def __init__(self,name):
        self.name=name
    def  display(self):
        print("viggie")
class p2(p1):
    def __init__(self,age):
        self.age=age
        super().__init__("ok")
        self.age=age
    def display(self):
        print("yes")
        print(self)
class c(p2):
    def __init__(self,id):
        self.id=id
        super().__init__("Done")
    def display(self):
        print("perfect")
obj=p2(32)
obj1=c(72)
obj.display()

