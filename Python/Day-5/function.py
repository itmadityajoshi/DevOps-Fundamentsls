def greet(name):
    return f"Hello,{name}!"
print(greet("Alice"))



#1. Positional Arguments 
def add(a,b):
    return a+b
print(add(5,3))

#2. Default Arguments
def greet(name="Guest"):
     return f"Hell0, {name}!"
print(greet())

#3. Keyword Arguments
def student(name, age):
     print(f"Name: {name}, Age:{age}")

student(age = 28,name="Bhim")


#Lambda Function in Python

#Lambda functions are anonymous, inline functions.

#syntax:

square = lambda x: x *x
print(square(4))