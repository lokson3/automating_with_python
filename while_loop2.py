username = 'user1234'
password = 'passcode'
attempts = 0
while attempts < 3:
	username = input('username: ')
	password = input('password: ')
	if username != 'user1234' and  password != 'passcode':
		print('wrong password or wrong username')
	else:
		print('login successful!')
		break
	attempts = attempts + 1
	
