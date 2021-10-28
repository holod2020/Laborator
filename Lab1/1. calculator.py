def calculator(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a*b
    elif c == "/":
        return a/b
    else:
        return "operation"
result = calculator (int(input("Enter number:  ")), 
                     int(input("Enter number: ")), 
                     input("Enter operation:"))

print("Result : ", result)