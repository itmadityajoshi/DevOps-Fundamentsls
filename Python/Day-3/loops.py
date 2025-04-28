fruits = ["apple","banana","cherry"]

for f in fruits:  #f is used to denoate each item in fruits, iterations are done over them.
    print(f)




#using range() function

for i in range(6):
    print(i)


#while loop

count = 0


while count < 5:
    print("while loops is running....")
    print(count)
    count += 1


#Break statement
for i in range(10):
        if i == 5:
            break
        print(i)  #o/p--> 0,1,2,3,4


#continue

for i in range(5):
    print('continue')
    if i ==2:
        continue
    print(i)

#pass

    for i in range(5):
        if i ==3:
            pass
        print(i)