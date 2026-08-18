class A:
	def __init__(self, name):
		self.name=name

class B(A):
	pass

a=A("Raj")
print(a.name)
b=B("Manu")
print(b.name)

# the above one is public and we can access by calling using object

class M:
	#_name="Taru"
	def __init__(self, name):
		self._name=name

class N(M):
	pass

m=M("Mani")
print(m._name)
n=N("Nani")
print(n._name)

# the above one is protected and we can access this directly using _

class First:
	def __init__(self, name):
		self.__name=name

	def getName(self):        #to access the private class we need to use method and use return keyword
		return self.__name

class Second(First):
	pass

f=First("Surya")
print(f.getName())
s=Second("Surya")
print(s.getName())

#the above one is private and we cannot access directly using __. We should use function called "return method" - getName to access

#access specifier
#public (access to everyone) || private (only me) || protected(only selected my contacts)


