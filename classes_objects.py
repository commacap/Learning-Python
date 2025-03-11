class Character:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed

warrior = Character(100, 50, 90)
ninja = Character(100, 30, 110)

print(f'Warior speed: {warrior.speed}')
print(f'Ninja speed: {ninja.speed}')

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("Sam",36)

print(p1)