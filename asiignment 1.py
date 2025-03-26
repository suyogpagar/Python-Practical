
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes a '{self.sound}' sound"


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

    def show_info(self):
        return f"Dog Name: {self.name}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def show_info(self):
        return f"Cat Name: {self.name}, Color: {self.color}"


def describe_animal(animal):
    return animal.make_sound()


dog = Dog("Buddy", "bark", "Golden Retriever")
cat = Cat("Whiskers", "meow", "Tabby")


print(dog.show_info())
print(cat.show_info())
print(describe_animal(dog))
print(describe_animal(cat))
