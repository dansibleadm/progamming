from random import randint


""" Task 1 """

numbers_1 = [randint(0, 100) for i in range(0, 10)]
print('First list: %s' % numbers_1)

numbers_2 = [num for idx, num in enumerate(numbers_1) if idx % 2 == 0]
print('Second list: %s' % numbers_2)

""" Task 2 """

numbers_3 = []
for i, value in enumerate(numbers_1):
	if i == 0:
		numbers_3.append(value)
	else:
		if value > numbers_1[i - 1]:
			numbers_3.append(value)

print('Third list: %s' % numbers_3)

""" Task 3 """

max_n = {0:0}
min_n = {0:100}

for key, num in enumerate(numbers_1):
	if int(list(max_n.values())[0]) < num:
		max_n = {key: num}
	if int(list(min_n.values())[0]) > num:
		min_n = {key: num}

numbers_1[list(max_n.keys())[0]] = int(list(min_n.values())[0])
numbers_1[list(min_n.keys())[0]] = int(list(max_n.values())[0])

print("Min: %s\tMax: %s\nFourth list: %s" % (min_n, max_n, numbers_1))