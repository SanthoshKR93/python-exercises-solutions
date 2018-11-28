import re
robj=re.compile(r'agent (\w)\w*')
mo=robj.sub(r'\1*****','agent carter is in india')
print(mo)
