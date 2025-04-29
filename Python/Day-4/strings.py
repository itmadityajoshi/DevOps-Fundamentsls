# singel-quoted string
a = 'Hello string'
print(a)

# dobule-quoted string
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
print(text.strip()) # remove all the unncessary spaces
print(text.replace("World", "Python")) 
print(text.split())

print("---------------------------------")
