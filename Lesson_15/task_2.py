# Doggy age

# Create a class Dog with class attribute 'age_factor' equals to 7. 
# Make __init__() which takes values for a dog’s age. 
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog():
    age_factor = 7

    def __init__(self, dogs_age):
        self.dogs_age = dogs_age

    def human_age(self):
        return Dog.age_factor * self.dogs_age
    
dog = Dog(3)

print(f"Dog's age in human years: {dog.human_age()}")
