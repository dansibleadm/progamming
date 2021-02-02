# Task 2

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.info("Init")

try:
	string = str(input("Enter string>"))
except Exception as exc:
	logging.error(f"{exc}", exc_info=True)

try:
	if string.__class__ == type(str()):
		logging.info("Find substrings without repeats...")
		substring = ""
		substrings = []

		for char in string:
			if char not in substring:
				substring += char
			else:
				substrings.append(substring)
				substring = ""

		logging.info("Find the longest substring...")
		max_lenght = 0
		for item in substrings:
			if len(item) > max_lenght:
				max_lenght = len(item)

		logging.info(f"The longest substring has lenght {max_lenght}")
except Exception as exc:
	logging.error(f"{exc}", exc_info=True)
