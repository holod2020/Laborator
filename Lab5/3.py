s=[]; summa=0
for i in range (0,15):
    summa+=i
    s.append(i)

print (('+').join(map(str,s)),'=',summa)