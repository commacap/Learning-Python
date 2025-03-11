class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def introduce_self(self):
        print("Hello! I am " + self.name)
    
p1 = Person("Sam",27)
p1.introduce_self()