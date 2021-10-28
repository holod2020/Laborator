# x1 = int(input('Вектор х1: '))
# x2 = int(input('Вектор х2: '))
# y1 = int(input('Вектор y1: '))
# y2 = int(input('Вектор y2: '))
from math import sqrt, acos, degrees
 
x1 = int(input('Вектор х1: '))
x2 = int(input('Вектор х2: '))
y1 = int(input('Вектор y1: '))
y2 = int(input('Вектор y2: '))
 
def scalar(x1,x2,y1, y2):
    return x1*x2 + y1*y2
 
def module(x, y):
    return sqrt(x ** 2 + y ** 2)
 
cos = scalar(x1, x2, y1, y2)/(module(x1,y1)*module(x2,y2))
 
ang = acos(cos)
 
print(degrees(acos(cos)))