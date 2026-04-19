
#* A+B
#* A,B is Operator
#* + is Operand

#* Arithmetic Operators + - * / % ** //

num01,num02 = 10,3
print("N01 = ",num01+num02)
print("N02 = ",num01-num02)
print("N03 = ",num01*num02)
print("N04 = ",num01/num02)
print("N05 = ",num01%num02)
print("N06 = ",num01**num02)
print("N07 = ",num01//num02)

#* Assignment Operators += -= *= /= %= **= //=  Ex.X+=Y is X=X+Y

x,y=20,6
x+=y
x-=y
x*=y
x/=y
x%=y
x**=y
x//=y
print("x = ",x)

#* Comparison Operators == != > < >= <=

x,y = 100,50
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#* Logical Operators and or not

username = input("name: " )
password = input("password: ")

if username == "admin" and password == "123456789":
    print("pass")
elif username == "admin" or password == "123456789":
    print("user OK but password wrong")
else:
    print("all wrong")

#* Identity Operators is , is not (same or not)

colorA = ["A","B","C"]
colorB = ["A","B","C"]
print(colorA is colorB) #! A and B are not the same.
data = colorA #* copy colorA
print(colorA is data)

#* Membership Operators in , not in (in the group or not)

colors = ["red","green","blue"]
print("red"in colors)
