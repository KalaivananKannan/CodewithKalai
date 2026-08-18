class A:
    def __init__(self):
        self.name='hi'


class B:
    def __init__(self):
        self.age=20


class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)


c= C()
print(c.name)
print(c.age)
