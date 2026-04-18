
#* While Loop unknown number of iterations

x = 0
while x<10:
    x+=1

#* For Loop known number of iterations

y = 1
for y in range(0,5): #! Python don't have block scope (use the same variable)
    print(y)
    y+=10
    break #* stop and end loop

y = 2
for i in range(0,5): #! 0(do1) 1(do2) 2(do3) 3(do4) 4(do5) 5(stop/not enter loop) 
    print(y)
    continue #* stop and loop again 
    y+=10

y = 3
for j in range(5,1,-2):
    print(y)
    y+=10

#* Nested-Loop loop in loop

for i in range(0,2):
    print("A")
    for j in range(0,4):
        print("B")