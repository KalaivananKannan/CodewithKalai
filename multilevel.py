class Bird1:
    def __init__(self):
        self.name="Hen"

class Bird2:
    def __init__(self):
        self.name="Myna"

class Myna(Bird2):
    def __init__(self):
        super().__init__()
        self.sound="soft voice"
        self.eat="fruits"

class Chick(Myna):
    def __init__(self):
        super().__init__()
        self.size="10"

chick=Chick()
print("Bird Name: "+ chick.name)
print("Bird Sound: "+ chick.sound)
print("Bird Food: "+ chick.eat)
print("Bird size: "+ chick.size)