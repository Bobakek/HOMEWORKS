class Horse:

    def __init__(self, x_distance = 0, sound = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += dx



class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self, x_distance= 0,  y_distance = 0, horse_sound='Frrr', eagle_sound='I train, eat, sleep, and repeat'):
        Horse.__init__(self, x_distance, horse_sound)
        Eagle.__init__(self, y_distance, eagle_sound) ## вопрос- у нас же методом super можно инициализацию вызвать только первого класса?.  то есть для HORSE я могу его использовать а для EAgle не могу уже???
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)



    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        return f'Horse sound: {self.sound}, Eagle sound: {self.sound}'

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
