#! python3
# pw.py - an insecure password locker program

PASSWORDS = {'email': 'Jon123!@#',
			'blog': 'Roger456$%^', 
			'luggage': '12345'}

import sys
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]     # first command line arg is the account name 