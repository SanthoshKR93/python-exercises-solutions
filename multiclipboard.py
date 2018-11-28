#! python3
# code to create multiclipboards
import pyperclip,shelve,sys
ms=shelve.open('multiclipboard')      #create shelve ms
if len(sys.argv)==3 and str(sys.argv[1]).lower()=='save':    #save clipboard content to shelve
    ms[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if str(sys.argv[1]).lower()=='list':
        pyperclip.copy(str(list(ms.keys())))
    elif sys.argv in ms:
        pyperclip.copy(ms[sys.argv])

ms.close()
