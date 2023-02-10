# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел A. Последняя строка содержит число X


from random import randint

size = int(input('Введите N: '))
num = tuple(randint(1,size) for _ in range(size))
print(*num)
num_X = int(input('Введите число, к которому нужно найти ближайшее по величине: '))
mod = 0
flag = False
for _ in range(len(set(num))):
	for i in set(num):
		if i == num_X-mod or i == num_X+mod:
			print(i)
			flag = True
			break
	if flag:
		break
	mod += 1
