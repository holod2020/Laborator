y = int(input())
if y % 4 != 0:
    print("Обычный")
elif y % 100 == 0:
    if y % 400 == 0:
        print(True)
    else:
        print(False)
else:
    print("Високосный")
