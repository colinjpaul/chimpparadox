class Frood:
    def __init__(self, age):
        self.age = age
        print("Frood initialised")

    def anniversary(self):
        self.age += 1
        print("Frood is now {} years old".format(self.age))


f1 = Frood(12)
f2 = Frood(13)
f1.anniversary()
f2.anniversary()
