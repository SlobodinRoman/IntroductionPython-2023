# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел A.
# Последняя строка содержит число X

from random import randint

size = int(input('Введите N: '))
num_list = [randint(1,size) for _ in range(size)]
print(*num_list)
print(num_list.count(int(input('Введите число, которое хотите проверить: '))))