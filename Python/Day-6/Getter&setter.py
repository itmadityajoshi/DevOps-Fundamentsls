'''Getters and setters are methods that you create to control how attributes of your class are accessed and modified.
    They are a key part of the principle of encapsualtion.

    
Why use them?
 Validation: You can add checks within the setter to make sure the attribute is
 set to a valid value. For example, you could prevent an age from being
 negative.

 Read-Only Attributes: You can create a getter without a setter, making the
 attribute effectively read-only from outside the class. This protects the
 attribute from being changed accidentally.

 Side Effects: You can perform other actions when an attribute is accessed or
 modified. For instance, you could update a display or log a change whenever a
 value is set.

 Maintainability and Flexibility: If you decide to change how an attribute is
 stored internally (maybe you switch from storing degrees Celsius to
 Fahrenheit), you only need to update the getter and setter methods. You don’t
 need to change every other part of your code that uses the attribute. This
 makes your code much easier to maintain and modify in the future.
'''



class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age    

    def get_age(self):   #Getter for age
        return self._age
    
    def set_age(self, new_age):  #setter for age
        if new_age >= 0 and new_age <= 150:
            self._age = new_age
        else:
            print("Invalid age!")



person = Person("Masis", 29)
print(person.get_age())


person.set_age(30)
print(person.get_age())