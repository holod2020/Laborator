import numpy as np
l = int(input('Число 1: ')), int(input('Число 2: ')), int(input('Число 3: ')), int(input('Число 4: '))
l_sort = np.sort(l) #сортировка элементов списка
evens = list(filter(lambda x: x%2==0, l_sort)) #извлечение четных
odds = list(filter(lambda x: x%2!=0, l_sort)) #ивлечение нечетных
print('Парні: ', evens)
print('Непарні: ', odds)