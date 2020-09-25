"""
Format 
EMAIL | NAME | LAST_NAME | TEL | CITY 

Requirements:
- Read file
- Include generating func of emails
- Fil email-columns and rewrite source-file
- Email must be generated for those who have a name, last name, tel, city
- Tel number validating (7 nums) 
"""
import logging

from uuid import uuid4

class Pasrer:

	def __init__(self, file, accounts=[], new_accounts=[]):
		self.filename = file
		self.accounts = accounts
		self.new_accounts = new_accounts

	def start(self):
		self.read_file()
		self.set_emails()
		self.write_file()
		self._lprint("Done!")

	def read_file(self):
		try:
			with open(self.filename) as file:
				for line in file:
					self.accounts.append(line.split(','))
				self.accounts.pop(0)		
		except Exception as exp:
			logging.exception(exp)

	def write_file(self):
		buff = ""
		for account in self.new_accounts:
			buff += ', '.join(account)

		self.new_accounts = buff
		with open("new_" + self.filename, "w") as file:
			file.write('EMAIL, NAME, LAST_NAME, TEL, CITY\n')
			file.write(self.new_accounts)

	def set_emails(self):
		emails = []

		for account in self.accounts:

			valid_info = self.check_info(account)
			valid_tel = self.check_tel(account[-2]) if valid_info else False
			if valid_tel and valid_info:
				email = "%s.%s-%s@company.io" % (account[0].strip(), account[1].strip(), str(uuid4())[0:9])
				self.new_accounts.append([email, *account[1:]])
			else:
				self._lprint('Not valid tel or info: %s' % account)

	def check_tel(self, tel):
		tel = tel.strip()
		if len(tel) == 7 and tel.isdigit():
			return True
		else:
			return False

	def check_info(self, account):
		check = False
		account.pop(0)
		for value in account:
			value = value.strip()
			if len(value) > 1:
				check = True
			else:
				return False
		return check

	""" PRIVATE SECTION """

	def _lprint(self, data):
		return print("[*] %s" % data)

if __name__ == "__main__":
	parser = Pasrer(file="task_file.txt")
	parser.start()