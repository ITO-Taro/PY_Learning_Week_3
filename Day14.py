from os import PRIO_USER, pipe


num0 = []
for i in range(1, 6):
    num0.append(i)
num1 = []
for i in range(6, 11):
    num1.append(i)
num2 = []
for i in range(11, 16):
    num2.append(i)
l0 = ["abc", "def", "ghi"]
l1 = ['a', 'R', 'y', 'H', 'g', 't', 'Y', 'a', 'e']
t0 = ('0', '1', '2', '3', '4', '5')
t1 = [('TI', '03/26/1985', '131lbs'), ('MM', '04/22/1990', '150lbs')]

# def c3(x):
#     return x ** 3
# cubed = list(map(c3,num0)
    
# cubed = list(map(lambda x: x ** 3, num0))
# print(cubed)

# 1. program which triple all numbers of a given list of integers. Use map
triple = list(map(lambda x: x * 3, num0))
print(triple)

# 2. program to add three given lists using Python map and lambda
listadd = list(map(lambda x, y, z: x + y + z, num0, num1, num2))
print(listadd)

# 3. Write a Python program to listify the list of given strings individually using Python map.
listify = list(map(lambda x: list(x), l0))
print(listify)

# 5. program to square the elements of a list using map() function
sq = list(map(lambda x: x ** 2, num0))
print(sq)

# 6. program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence. Use map() function
def problem6(x):
    return str(x).upper(), str(x).lower()
print(set(list(map(problem6, l1))))

# 7. Write a Python program to add two given lists and find the difference between lists. Use map() function.
def addsub(x,y):
    return x+y, x-y
print(list(map(addsub, num0, num1)))

# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings
print(list(map(str, num0)), tuple(map(str, t0)))

# 9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to integer
print(list(map(lambda x: int(x[2][:-3]), t1)))
    

# problem6vari = ("abCD", "EFg", "hiiijk", "Klm", "Klm")
# def problem6basic(x):
#     return str(x).upper(), str(x).lower()
# print(problem6basic(problem6vari))

# MAPPING
evenNums0 = list(map(lambda x: x%2 == 0, range(1, 11)))
# print(evenNums0)

# LIST COMPREHENSION
evenNums1 = [x for x in range(1, 11) if x%2 == 0]
# print(evenNums1)

# FILTERING
evenNum2 = list(filter(lambda i : i % 2 == 0, range(1, 11)))
# print(evenNum2)

dict0 = {}
for i in range(11):
    if (i%2 == 0):
        dict0[i] = i**2
# print(dict0)

dict1 = {x:x**2 for x in range(11)}
# print(dict1)

dict2 = {x:x**2 for x in range(11) if x%2 == 0}
# print(dict2)

fahrenheit = {'t0': 10, "t1": 20, "t2": 30, "t3": 40, "t4": 50}
celsius = list(map(lambda x: (float(5)/9) * (x-32), fahrenheit.values()))
print(celsius)

dict3 = dict(zip(fahrenheit.keys(), celsius))
print(dict3)

dict4 = {k:(float((5)/9)*(v-32)) for (k,v) in fahrenheit.items()}
print(dict4)

dict5 = {k:(float((5)/9)*(v-32)) for (k,v) in fahrenheit.items() if v < 40}
print(dict5)

print(len("\n"))