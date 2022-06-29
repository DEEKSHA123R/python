class A:
    def test1(self):
        print("from test")

class B:
    def test2(self):
        print("from test2")

class C(A,B):
    def test3(self):
        print("from test3")
c1=C()
c1.test1();
c1.test2();
c1.test3();
print(issubclass(c,b))