import re
robj=re.compile(r'RoBoCOp',re.I)
mo=robj.search('robocop is the coolest cop')
print(mo)
