"""Map Function"""

listNumber = [1, 2, 3, 4, 5]
sonuc = list(map(lambda x: x ** 2, listNumber))
# [1, 4, 9, 16, 25]
print(sonuc)


# Rectangular area calculation

def AreaCalculate(tuple):
    return tuple[0] * tuple[1]


edgeValues = [(3, 4), (10, 3), (5, 6), (1, 9)]
print(list(map(AreaCalculate, edgeValues)))


"""Reduce Function"""

from functools import reduce

result=reduce(lambda x,y : x+y , [5,15,25,30,45])
print("Result of Reduce function  : {}".format(result))


"""Filter Function"""

result = list(filter(lambda x: x % 2 == 0, range(0, 25)))
print(result)

# IsTriangle

def IsTriangle(tuple):
    if (abs(tuple[0] + tuple[1]) > tuple[2] and abs(tuple[0] + tuple[2]) > tuple[1]
            and abs(tuple[1] + tuple[2]) >
            tuple[0]):
        print("This is a trinangle : {}".format(tuple))
    else:
        return False


edgeValues = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]
list(filter(IsTriangle, edgeValues))

"""Zip Function"""

list1 = [1, 2, 3, 4]
list2 = ["Python", "Java", "C#", "JS", "PHP"]

for i, j in zip(list1, list2):
    print(i, j)

"""Enumerate Function"""

listX=["C", "C++", "C#"]
print(list(enumerate(listX)))
