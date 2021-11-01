a = int(input('число 1: '))
b = int(input('число 2: '))
c = int(input('число 3: '))
mx = a 
if b > mx:
    mx= b
if c > mx:
    mx = c
print('большое: ', mx)
mn = a 
if b < mn:
    mn= b
if c < mn:
    mn = c
print('меншое: ', mn)
