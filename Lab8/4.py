def useless(lst):
    return max(lst) / len(lst)

print(useless([1, 7, 56]))
print(useless([25, -4, 13, 9, 0, 6]))
print(useless([45, -55, -4.56, -0.6, 11.2, 12, 9.1]))