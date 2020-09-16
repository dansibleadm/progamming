password = input('Enter the pasword: ')
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '\'', '\"', ',', '.']
level = ''

if len(password) >= 12:
	for sym in symbols:
		if sym in password:
			level = 'Too simple'
			break
	for c in password:
		if c.isdigit():
			level = 'Normal'
			break
	for c in password:
		if c.isupper():
			level = 'Hard'
			break
else
	level = 'Too short'

print(level)