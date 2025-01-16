class Pet:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
        self.energy = 100

    def eat(self, food_amount):
        self.energy += food_amount
        print(f"{self.name} has eaten and now has {self.energy} energy.")

    def sleep(self, hours):
        self.energy += hours * 10
        print(f"{self.name} slept for {hours} hours and now has {self.energy} energy.")

    def play(self, play_time):
        self.energy -= play_time * 5
        print(f"{self.name} played for {play_time} minutes and now has {self.energy} energy.")

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age, "cat")

    def meow(self):
        print(f"{self.name} says 'Meow!'")

my_cat = Cat("Whiskers", 3)
my_cat.meow()
my_cat.eat(20)
my_cat.play(30)
my_cat.sleep(2)
