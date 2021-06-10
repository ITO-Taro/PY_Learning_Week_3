# def drinkAge():
#     yourAge = int(input("How old are you?: "))
#     if (yourAge >= 21):
#         print("Beer, Whiskey, Mix-drink?")
#     else:
#         print("Please Leave")

# yourAge = int(input("How old are you?: "))
# drink = "Beer, Whiskey, Mix-drink?" if yourAge >= 21 else "Please Leave"

# print(type(drink))
# print(drink)



add0 = lambda x, y : x + y
# print(add0(3, 10))

# def addcon(x, y):
#     if (x + y) > 21:
#         return True
#     else:
#         return False

# def specialAdd(x, y):
#     if (x + y) > 21:
#         return True
#     else:
#         return False

# def specialAdd0(x, y):
#     return True if (x + y) > 21 else False

# print(specialAdd(10, 5))
# print(specialAdd0(10, 5))

# specialAdd1 = lambda x, y : True if ((x+y)> 21) else False
# print(specialAdd1(10, 19))

# l0 = [1, 3, 5, 7, 9]
# l1 = []
# for i in range(len(l0)):
#     l1.append(l0[i] ** 2)

# print(l1)

l2 = []
for i in range(10):
    l2.append(i)

l2 = [i+1 for i in range(10)]
print(l2)

# FUNCTION CALLED "EVENNUMS" THAT TAKES IN A LIST OF NUMBERS AS A PARAMETER/ARGUMENT, AND RETURNS A NEW LIST WITH ONLY THE EVEN NUMBERS (lambda, list comprehension, ternary)
def evenNums():
    l3 = []
    for i in range(1, 11):
        if (i%2 == 0):
            l3.append(i)
l4 = []
evenNum1 = list(filter(lambda i : i % 2 == 0, range(11)))
print(evenNum1)


