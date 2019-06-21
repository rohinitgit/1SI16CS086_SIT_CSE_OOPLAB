import sys, pyperclip

PASSWORDS = {'email': 'TGSCHGCHGSCGHncjc',
             'fbaccount': 'SUGUKSGUhFJHFvvsfsyu',
             'instagram': 'schJH SJFSFhfjsf',
             'twitter':'HSHDSHDsgcdsgdghadHGDAT',
             'snapchat':'HDHGsbhfsyhfdjhtfudgGSUT'}	

if len(sys.argv) < 2:
	print('Usage: python passmanager.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]	
#account=input()

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
