# Task 1

import logging

from collections import Counter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.info("Init")

try:
	arr = str(input("Enter original list (example: 1,2,3)>")).split(',')
	brr = str(input("Enter second list>")).split(',')
	logging.info(f"{arr} -> len({len(arr)})")
	logging.info(f"{brr} -> len({len(brr)})")

	arr_count = dict(Counter(arr))
	brr_count = dict(Counter(brr))
	found = []

	for key, value in arr_count.items():
		if key not in brr:
			for i in range(arr_count[key]):
				brr.append(key)
				found.append(key)
			brr_count = dict(Counter(brr))
		else:
			if value > brr_count[key]:
				for i in range(value-brr_count[key]):
					found.append(key)

	logging.info(f"Lost items: {found}")
except Exception as exc:
	logging.error(f"{exc}", exc_info=True)