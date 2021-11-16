import numpy
from prettytable import PrettyTable


def getFile():
    text = []
    with open("lab2.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            text.append(i.replace('\n', ''))
    for i in range(len(text)):
        text[i] = text[i].split(" ")
    return text


def tree(array):
    a = array[0][2] * array[0][1] * 5 + array[0][4] * array[0][3] * 5 - array[0][0]
    b = array[1][2] * array[1][1] * 5 + array[1][4] * array[1][3] * 5 - array[1][0]
    
    d = array[2][2] * array[0][1] * 4 + array[2][3] * array[0][3] * 4 - array[0][0]
    e = array[2][2] * array[1][1] * 4 + array[2][3] * array[1][3] * 4 - array[1][0]
    
    cPlus = numpy.max([d, e])
    c = array[2][0] * cPlus + array[2][1] * 0
    
    root = numpy.max([a, b, c])
    
    print("\tEmv(A):", a)
    print("\tEmv(B):", b)
    print("\tEmv(D):", d)
    print("\tEmv(E):", e)
    print("\tEmv(C+):", cPlus)
    print("\tEmv(C):", c)
    print("\tEmv(Main):", root)

    if root == a:
        print("version: A")
    elif root == b:
        print("version: B")
    elif root == c:
        if c == d:
            print("version: C-D")
        elif c == e:
            print("version: C-E")

array = getFile()
array = [[int(j) if '.' not in j else float(j) for j in i] for i in array]

table = PrettyTable(['version', 'M1', 'D1', 'P1', 'D2', 'P2'])
table.add_row(['A', array[0][0], array[0][1], array[0][2], array[0][3], array[0][4]])
table.add_row(['B', array[1][0], array[1][1], array[1][2], array[1][3], array[1][4]])
print(table)
table = PrettyTable(['version', 'P3', 'P4', 'P1', 'P2'])
table.add_row(['C', array[2][0], array[2][1], array[2][2], array[2][3]])
print(table)

tree(array)
