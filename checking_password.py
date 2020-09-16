from hashlib import md5
from base64 import b64encode

from getpass import getpass

password = getpass('Enter the pasword: ')
level = ''

if len(password) >= 12:
	for c in password:
		if ord(c) in range(33, 48):
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
else:
	level = 'Too short'
	exit()

print(level)
print('Your password {}'.format(md5(b64encode(password.encode())).hexdigest()))