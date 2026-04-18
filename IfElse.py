x = 10
#* if Statement
#* if

if x != 10:
    x = 100

#* if-else

if x != 10:
    x = 100
else:
    x = 1000
#? Ternary Operator (1 value)
x = 100 if x != 10 else 1000

#* if-elif-else

if x == 100:
    x = 10
elif x == 111:
    x = 11
else:
    pass #* Let it pass for now

#* Nested-if if in if in if...

user = "member"
password = "1234"
number_of_use = "2"
if user == "member" and password == "1234":
    print("login OK")
    if number_of_use == "1":
        print("A")
    if number_of_use == "2":
        print("B")
    if number_of_use != "1" and number_of_use != "2":
        print("XXX")
else:
    print("Can't login")

#* Match Statement case
NumBank = "4"
match NumBank:
    case "1":print("1")
    case "2":print("22")
    case "3":print("333")
    case "4":print("4444")
    case _:print("what is this?") #! เหมือน else
