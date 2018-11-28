import requests
result=requests.get('https://drive.google.com/file/d/1OTio2-hSqdMM-TjwnVbdJ0dPgUVCv1Pu/view?usp=sharing')
try:
   result.raise_for_status()
except Exception as exp:
       print('exception is %s'%(exp))
file=open('result.txt','wb')
for chunks in result.iter_content(100000):
    file.write(chunks)
file.close()
