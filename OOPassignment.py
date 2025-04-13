# assignment1
class Superhero:
    def __init__(self, name, power, secret_identity):
        # Constructor to initialize attributes
        self.name = name
        self.power = power
        self.__secret_identity = secret_identity  # Private attribute (encapsulation)

    def introduce(self):
        return f"I'm {self.name}, and my power is {self.power}!"

    def reveal_secret(self):
        return f"My secret identity is {self.__secret_identity}. 🤫"

# Inheritance: Creating a subclass 
class Sidekick(Superhero):
    def __init__(self, name, power, secret_identity, mentor):
        super().__init__(name, power, secret_identity)
        self.mentor = mentor

    def introduce(self):  # Override the parent method
        return f"I'm {self.name}, sidekick to {self.mentor}! My power is {self.power}."

# Example usage
hero = Superhero("Captain Python", "code generation", "Alex")
sidekick = Sidekick("Debugger Boy", "fixing bugs", "Sam", "Captain Python")

print(hero.introduce())          
print(sidekick.introduce())      
print(sidekick.reveal_secret())


#assignment 2

class Animal:
    def move(self):
        pass  # Abstract method

class Dog(Animal):
    def move(self):
        return "Running on four legs! "

class Fish(Animal):
    def move(self):
        return "Swimming gracefully!"

class Bird(Animal):
    def move(self):
        return "Soaring through the sky! "

# Polymorphism in action
animals = [Dog(), Fish(), Bird()]
for animal in animals:
    print(animal.move())

