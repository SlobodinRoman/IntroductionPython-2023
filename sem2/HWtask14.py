# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N=int(input('Введите N: '))
two_power,power=1,1
while two_power<=N:
	print(two_power,end=' ')
	two_power=2**power
	power+=1
