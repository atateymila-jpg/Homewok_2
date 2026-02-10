import random

class Parrot:
    def __init__(self, name):
        self.name = name
        self.energy = 50
        self.mood = 50
        self.activity = 50
        self.alive = True

    def to_fly(self):
        print("Time to fly")
        self.energy += 5
        self.mood -= 3
        self.activity += 5

    def to_eat(self):
        print("Time to eat")
        self.energy += 9
        self.mood += 4
        self.activity += 5

    def to_sing(self):
        print("Time to screm!")
        self.energy -= 10
        self.mood += 8
        self.activity -= 8

        def to_activity(self):
            print("Time do some thing")
            self.energy -= 9
            self.mood += 8
            self.activity = 50

    def is_alive(self):
        if self.energy <= 0:
            print("The parrot was tired...")
            self.alive = False
        elif self.mood <= 0:
            print("The parrot was bored...")
            self.alive = False
        elif self.energy > 100:
            print("The parrot ate a lot.")
            self.alive = False
        elif self.activity > 100:
            print("The parrot wasn't know what to do.")
            self.alive = False


    def end_of_day(self):
        print(f"Energy = {self.energy}")
        print(f"Mood = {self.mood}")
        print(f"activity = {self.activity}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(day)

        live_cube = random.randint(1, 3)

        if live_cube == 1:
            self.to_fly()
        elif live_cube == 2:
            self.to_eat()
        elif live_cube == 3:
            self.to_sing()
        elif live_cube == 4:
            self.to_do()

        self.end_of_day()
        self.is_alive()


parrot = Parrot("Sky")
print(parrot.name)

print("Energy:", parrot.energy)
print("Mood:", parrot.mood)
print("Alive?", parrot.alive)
print("activity", parrot.activity)

for day in range(67):
    if not parrot.alive:
        break
    parrot.live(day)
