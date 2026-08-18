class A:
    def __init__(self, username, password):
        self.__username=username
        self.__password=password
    def getusername(self):
        return self.__username
    def getpassword(self):
        return self.__password
class B(A):
    pass
a=A("Rahul", "IPCSglobal123")
print(a.getusername())
print(a.getpassword())
b=B("Mani", "IPCSglobal124")
print(b.getusername())
print(b.getpassword())