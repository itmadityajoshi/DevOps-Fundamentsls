#Age Group Calculations
""" classify a person's age group: child(<13), Teenager(13-19), Adult(20-59), Senior(60+)"""


# age = int(input("Enter the age : "))

# if age < 13:
#     print('You are child.')
# elif age>=13 and age <=19:
#     print("You are a Teenager.")
# elif age>=20 and age <= 59:
#     print("You are an Adult.")
# else:
#     print("You are a Senior person.")




''''Movie Tickets are priced based on age: $12 for adults(18 and over), $8 for children. Everyone gets a $2 discount on wednesday'''


age = int(input("Enter the age: "))
day = "wednesday"

if age >=18:
    print("Ticket Price is : $12 for an adult.")
elif age < 18:
    print('Ticket price is $8 for children.')
else day
    print("$2 Discount on Wednesday. ")