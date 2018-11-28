#! python3
# p1extractnumbersandemail.py - Finds phone numbers and email addresses on the clipboard.

import re,pyperclip
robj=re.compile(r'''(
(\+)?
(\d{2})
(\s|-|\.)?
(\d{10})
)''',re.VERBOSE)
robj1=re.compile(r'''(
[a-zA-Z0-9._%+-]+      # username
@                      # @ symbol
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})      # dot-something
)''',re.VERBOSE)
cbdata=str(pyperclip.paste())
found=[]
for groups in robj.findall(cbdata):
    phone=groups[0]
    found.append(phone)
for groups in robj1.findall(cbdata):
    found.append(groups[0])
if len(found) > 0:
    pyperclip.copy('\n'.join(found))
    print('Data copied to clipboard:')
    print('\n'.join(found))
else:
    print('Sorry!! no phone numbers or email addresses found.')
