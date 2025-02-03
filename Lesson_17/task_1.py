# Method overloading.

# Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their own implementation of the method talk be different. 
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.  

class Animal:
    def talk(self):
        pass

# Subclass Dog
class Dog(Animal):
    def talk(self):
        print("Woof woof!")

# Subclass Cat
class Cat(Animal):
    def talk(self):
        print("Meow!")

def make_animal_talk(animal):
    if isinstance(animal, Animal):
        animal.talk()
    else:
        print("Don't know this Animal.")

dog = Dog()
cat = Cat()

make_animal_talk(dog)
make_animal_talk(cat)
