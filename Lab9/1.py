def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst

print(list_sort([1, 2, 12]))
print(list_sort([12, 3, 6, -1, 0, 45]))
