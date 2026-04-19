
#* Dynamic Typing
#* Primitive Data Type
    #* int float complex = 10 99.99 3+5j
    #* bool = True|False
    #* str = "Hello Me"
    #* NoneType = It is used to hold data with an unpredictable or unknown type.

name = "cat"
age = 30
print(name,age)
print(type(name),type(age))
name,age = "dog",60
print(name,age)

#! Rule's Name of Value
#! YES A-Z a-z _, Case Sensitive
#! NO 1234567890A, {} [] () % ^  Empty space, keyword

#* Non-Primitive Data Type(Reference Data Types) List Tuple Set Dictionary
    #* List can be repeated and modified (ordered)  
        #* List Either the same or different data types. Start index = 0 , use [0,1,2] , Data in List call "element"

data1 = ["nan",1,True,12.36] 
data_not_have = [] #* not have data when start
data2 = list(("nan",1,True,25.36))
print(len(data1)) 
print(len(data_not_have)) 
print(len(data2)) 
        
        #* List + List

data_mix = data1 + data2
print(data_mix)

        #* in to List 0 1 2 ... or ... -3 -2 -1 it like String

print(data_mix[0:3])
print(data_mix[1:])

        #* Edit data in List

data_mix[0] = "hospital"
print(data_mix[0:3])

        #* function for List
list_me=["focus"]
            #* .append(element) add to the end 1 elements
list_me.append("blue")
print(list_me)
            #* .extend([element]) add to the end multiple elements
list_me.extend(["red","me","me"])
print(list_me)
            #* .insert(index,element) add new element by index 
list_me.insert(1,"me")
print(list_me)
            #* .remove(element) delete element from list
list_me.remove("red")
print(list_me)
            #* .count(element) count same data
print(list_me.count("me"))
            #* .sort()
list_me.sort()
print(list_me)
            #* .reverse() invert sort
list_me.reverse()
print(list_me)
            #* .clear() delete all element
list_me.clear()
print(len(list_me))

    #* Tuple can be repeated (ordered)
    #! but can't modified 
        #* Tuple Either the same or different data types. Start index = 0 , use (0,1,2) , Data in Tuple call "element"

word1 = (1,9,3)
word_none = ()
word2 = tuple((2,3,4))

print(len(word_none))

print(word1+word2)

word3 = word1*3
print(word3)

colors = ("red","green","blue")
R,G,B = colors #* R = "red" G = "green" B = "blue" (unpacking-list tuple string) 
R, *rest = colors #* R = "red" rest = "green,blue"(list)

        #* function for tuple
            #* .count(element)

print(word3.count(9))

            #* .index(element) look index of element

print(word3.index(1)) #! It finds only the closest position.
print(type(word3))

    #* Set is the same tuple
    #! can't modified can't be repeated not have index (unordered)
        #* Set Either the same or different data types. , use {0,1,2} , data in Set call "element"

set1 = {1,2,3};set_none = {};set2 = set((3,4,5))
print(len(set1))

            #* .add(element) 1 element

set1.add(4)
print(set1)

            #* .update((element)) multiple elements

set1.update({5,6,7,8,4,4,4,4,4,4})
print(set1)

            #* .discard(element) delete this element

set1.discard(2)
print(set1)

            #* .union() merge A set and B set

s1 = set1.union(set2)
print("s1 = ",s1)

            #* .intersection() element in A,B set have

e1 = set1.intersection(set2)
print("e1 = ",e1)

            #* .difference() have in A set but not have in B set

t1 = set1.difference(set2)
print("t1 = ",t1)

    #* Dictionary key --> value (key = index)
    #! key can't be repeated

dic01 = {
    "red":"R",
    "yellow":"Y"
}
print(dic01["red"])
dic01["yellow"] = "Yes" #* Edit
print(dic01["yellow"])
dic01["blue"] = "B" #* Add
print(dic01["blue"])

dic02 = {
    "Odd":[1,3,5,7,9],
    "Even":[2,4,6,8,10]
}
print(dic02["Even"])

        #* function for Dictionary
cold = {
    "Q":"q",
    "E":"e",
    "A":"a"
}
            #* .keys() all key in Dictionary

print(cold.keys())

            #* .values() all value in Dictionary

print(dic02.values())

            #* .get(key) get data by key

print(dic02.get("Odd"))

            #* .items() all key,value in Dictionary

print(cold.items())
print(dic02.items())

            #* .clear() delete all

cold.clear()
print(cold.items())

            #* .pop(key) delete data by key

dic02.pop("Odd")
print(dic02.items())

            #* .update({key:value}) add,update data 

dic02.update({"AAA":[12,56,98]})
print(dic02.items())
