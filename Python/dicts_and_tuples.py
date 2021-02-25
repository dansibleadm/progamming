from random import randint
from collections import Counter

""" Task 1 """

some_dict = {str(value): randint(0, 10) for value in range(0, 30)}

key = input('Введите ключ: ')

try:
	print("Key\tValue")
	print("%s\t%s" % (key, some_dict.get(key)))
except Exception as exc:
	print(exc)

""" Task 2 """

value = input('Введите значение: ')

try:
	print("Key\tValue")
	for key, vl in some_dict.items():
		if int(value) == vl:
			print("%s\t%s" % (key, vl))
except Exception as exc:
	print(exc)

""" Task 3 """

alphabet = ['apple', 'orange', 'pie']
strings = [alphabet[randint(0, 2)] for i in range(10)]
print(Counter(strings))