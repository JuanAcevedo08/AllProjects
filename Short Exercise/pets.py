class Pets:
    def __init__(self, name, species, energy, sound_type):
        self.name = name
        self.species = species
        self.energy = energy
        self.sound_type = sound_type

    def Play(self, toy):
        if self.energy > 10:
            print(f"Your {self.species} {self.name} is playing with {toy}")
            self.energy -= 10
        else:
            print(f"{self.name} is tired and needs to rest")

    def Eat(self):
        print(f"{self.name} is eating")

    def MakeSound(self, sound):
        print(f"Your {self.species} {self.name} is {self.sound_type} in its world, saying {sound}")

    def Rest(self):
        print(f"{self.name} is resting")
        self.energy = 100

# Creating pets or objects in OOP
dog = Pets("Doki", "Dog", 100, "barking")
cat = Pets("Garfield", "Cat", 100, "meowing")
rabbit = Pets("Bugs Bunny", "Rabbit", 100, "growling")

# Pets playing
dog.Play("bone")  # Output: Your Dog Doki is playing with bone
cat.Play("ball of yarn")  # Output: Your Cat Garfield is playing with ball of yarn
rabbit.Play("fake carrot")  # Output: Your Rabbit Bugs Bunny is playing with fake carrot

# Pets eating
dog.Eat()  # Output: Doki is eating
cat.Eat()  # Output: Garfield is eating
rabbit.Eat()  # Output: Bugs Bunny is eating

# Pets making sounds
dog.MakeSound("WOOF, WOOF, WOOF")  # Output: Your Dog Doki is barking in its world, saying WOOF, WOOF, WOOF
cat.MakeSound("MEOW, MEOW, MEOW")  # Output: Your Cat Garfield is meowing in its world, saying MEOW, MEOW, MEOW
rabbit.MakeSound("GROWL")  # Output: Your Rabbit Bugs Bunny is growling in its world, saying GROWL

# Pets resting
for _ in range(10):
    dog.Play("bone")  # This will tire the pet

dog.Rest()  # Output: Doki is resting
