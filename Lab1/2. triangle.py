import math 
a = int(input("Enter side a: ")) 
b = int(input("Enter side b: ")) 
#c = int(input("Enter side c: ")) 
f = (a+b)/2 
s = math.sqrt(f*(f-a)*(f-b))

print(s)
