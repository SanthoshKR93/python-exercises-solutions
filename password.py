#! python3.5.2
# program to store passwords
PASSWORDS={'facebook':'santo',
           'gmail':'warhawk',
           'github':'killbox'}
import sys,pyperclip
if len(sys.argv)<2:
   print('Usage: python password.py [account] - copy account password')
   sys.exit()
account=sys.argv[1]
if account in PASSWORDS:
   pyperclip.copy(PASSWORDS[account])
   print('the password for' + account + 'is copied to clipboard')
else:
   print('password for' + account + 'is not present')
