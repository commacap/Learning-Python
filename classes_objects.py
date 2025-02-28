class Character:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed

warrior = Character(100, 50, 90)
ninja = Character(100, 30, 110)

print(f'Warior speed: {warrior.speed}')
print(f'Ninja speed: {ninja.speed}')