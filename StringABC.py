A = "WOW"
B = "ABCDE"
print(A,B) 
#* Concatenation

C = A+B
print(C)
D = "AAA"+"BBB"
print(D)

#* Three Double Quote

E = """
AS ME
OH GOD
GG GOOD GAME
"""
print(E)

#* Format String
    #* f"{value}"

name = "Nan"
age = 20
print(f"My name is {name}, I am {age} years old")

    #* f"{Expression}"

a = 5
b = 3
print(f"Sum = {a + b}")

    #* f"{numberA:.decimal f}"

pi = 3.1415926535
print(f"{pi:.2f}")

    #* mix

price = 49.5
print(f"Price: {price:.2f} Baht")

    #* age = f"i am {2569-number}"

#* Slice
    #* N a n   T O   M e 
    #* 0 1 2 3 4 5 6 7 8
    #*-9-8-7-6-5-4-3-2-1
    #*[index start:] 
    #*[:index final+1] 
    #*[index start:index final+1]

text = "Nan To Me"
print(len(text)) #* length of str
print(text[4:])
print(text[:3])
print(text[4:8])
print(text[-8:])
print(text[0:8:4]) #* +4 use 4 step

#* String Function name.function 
text = "AbCdEff"
text_me = "  AbCdEf  "
    #* .upper()
print(text.upper())
    #* .lower()
print(text.lower())
    #* .startswith(string) Start by ...
print(text.startswith("A"))
    #* .endswith(string) End by ...
print(text.endswith("f"))
    #* .find(string) find the position of a substring
print(text.find("dEf"))
    #* .count(string) count ...
print(text.count("A"))
    #* .replace(old,string) replace old with string
text = text.replace("Cd","555")
print(text)
    #* .strip() remove leading and trailing whitespace from a string
print(text_me.strip())
    #* .format()
name = "Nan"
age = 20
print("My name is {} and I am {} years old".format(name, age))

print("{0} {1} {0}".format("Hi", "Nan"))

print("My name is {name}".format(name="Nan"))

pi = 3.14159
print("{:.2f}".format(pi))

print("{:<10}".format("Hi"))  
print("{:>20}".format("Hi"))  
print("{:^10}".format("Hi"))

print("{:05}".format(42))

#* format
"Hello {}".format(name)
#* f-string (popular)
f"Hello {name}"