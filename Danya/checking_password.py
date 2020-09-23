from hashlib import md5
from base64 import b64encode

from getpass import getpass

password = getpass('[+] Enter the password: ')
level_dct = dict(level=0, levels=['Short', 'Simple', 'Normal', 'Hard'])

if len(password) >= 12:
	for c in password:
		if ord(c) in range(33, 48):
			level_dct['level'] += 1
			break
	for c in password:
		if c.isdigit():
			level_dct['level'] += 1
			break
	for c in password:
		if c.isupper():
			level_dct['level'] += 1
			break

print('[^] Level {level}\n[*] Your password {password}'.format(
																password=md5(b64encode(password.encode())).hexdigest(), 
																level=level_dct['levels'][level_dct['level']])
																)