# single-quoted string
from numpy.f2py.symbolic import as_ge

a = 'Hello string'
print(a)

# double-quoted string
d = "Double String"
print(d)

# Triple-quoted string

c = ''' This is a 
        multi-line 
        string'''

print(c)


print("-----------------------------------")

text = "Python"
print(text[0]) #Output: p
print(text[1]) # op --> y
print(text[-1]) #op--> n (last character)


#String Slicing
text = "Hello, Python!"

print(text[0:5]) #op ---> Hello 
print(text[:5])  #op ---> Hello
print(text[7:]) #op ----> Python!
print(text[:2]) #op ----> He
print(text[::2]) #op ---> Hlo yhn

print("-------------------------------------")


#sting Methods

text = " hello world "
print(text.upper())
print(text.lower())
print(text.strip()) # remove all the unnecessary  spaces
print(text.replace("World", "Python")) 
print(text.split())

print("---------------------------------")


#Common string Methods

text = "  Hello World  "

#removing Whitespaces
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print("----------------------------------")

#Finding and Replacing

text = "Python is Fun"

print(text.find("is"))
print(text.replace("Fun", "awesome"))



#Splitting and Joining

text = "apple,banana,orange"
fruits = text.split()    #create a list of fruits
print(fruits)

new_text = " - ".join(fruits)
print(new_text)
print(len(text))

#format() and f-strings

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

x =10
y =5
print(f"The sum of {x} and {y} is {x+y}.")


