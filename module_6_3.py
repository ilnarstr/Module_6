from random import random, randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords = [0, 0, 0]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you O_O")

    def speak(self):
        print(f'{self.sound}')

class Bird(Animal):
    def __init__(self, speed, _cords = [0, 0, 0], beak = True):
        super().__init__(speed, _cords)
        self.beak = beak

    def lay_eggs(self):
        print(f'Here are(is) {randint(1, 4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = int(self._cords[2] - self.speed / 2 * abs(dz))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = 'Click-click-click'

db =Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()