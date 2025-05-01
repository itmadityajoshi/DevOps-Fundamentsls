

class Dog: #we define a class called "Dog"
    species = "Bhote Kukur" # a class attribute  

    def __init__(self, name, breed): #The constructor 
        self.name = name # an instances attribute to store the information
        self.breed = breed # an instances attribute to store the information

    def bark(self): # a method (an action the can do)
        print(f"{self.name} says woof!")

# now, let's create some Dog Objects

my_dog = Dog("jammy","Bhote")  #create an object 
another_dog = Dog("Bannsi", "sherpa") # creating another object

#we can access their attributes

print(my_dog.name)   
print(another_dog.breed)

#And make them perform actions:

my_dog.bark()
another_dog.bark()

print(my_dog.species)


'''  
    self -- insida a class, self is like saying "the particular object". 
    It's a way for the obejct to refer to itself. it's always the first parameter in a method definition,
    but python handles it automatically when you call the method.
    you don not type self when calling the method, Python inserts it for you.

'''