class Base:
    def __init__(self, x):
        self.x = x

    def show(self):
        print('Base', self.x)


class Derivative(Base):
    def __init__(self):
        super().__init__(404)  # Явный вызов конструктора

    @staticmethod
    def say(txt: str):
        print(txt)


class Derivative2(Derivative):
    def __init__(self):
        Derivative.__init__(self)
        Base.__init__(self)  # Todo


a = Base(5)
b = Derivative()
c = Derivative2
a.show()
b.show()
b.say('Hello OOP')
c.say('Hello from Derivative2')
c.show()
