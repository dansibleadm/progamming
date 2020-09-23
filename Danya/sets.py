from random import randint

""" Task 1 """

list_1 = [randint(0, 10) for i in range(0, 10)]
print("Set 1: %s" % set(list_1))

""" Task 2 """

counter = 0
set_1 = set(list_1)
set_2 = set([randint(0, 10) for i in range(0, 10)])

for i in set_1:
	if i in set_2:
		counter += 1

print("\nSet 1: %s\nSet 2: %s" % (set_1, set_2))
print("Count: %s" % counter)

""" Task 3 """

if set_1.issubset(set_2) and (len(set_1) != len(set_2)):
	print('%s is subset of %s' % (set_1, set_2))