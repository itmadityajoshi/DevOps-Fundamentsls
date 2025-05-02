class Animal:    #parent class
    def __init__(self,name):
        self.name = name

    def speak(self):
        print('Animal makes different sound.')


class Dog(Animal):   #child class
    def speak(self):
        print("Bhau Bhau")

class Cat(Animal):   #child class
    def speak(self):
        print("meow")    


my_dog = Dog("Bhote")
print(my_dog.name)

my_cat = Cat("kitty")
print(my_cat.name)




#with super

# Calling Parent Constructor with super()
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name) # Call Animal's __init__ to set the name
        self.wingspan = wingspan # Add a Bird-specific attribute

my_bird = Bird("Tweety", 10)
print(my_bird.name)
# Output: Tweety (set by Animal's constructor)
print(my_bird.wingspan) # Output: 10   (set by Bird's constructor