figure = input('Назва фігури: ')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


match figure:
	case 'x1 == x2 or y1 == y2':
		print ('Tura')
	case abs(x1 - x2) == abs(y1 - y2):
		print('fezi')
