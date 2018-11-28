import bs4,requests
#requests module is only needed if we are downloading the data from internet
file=open('myfile.html')
bs4obj=bs4.BeautifulSoup(file)
pelement=bs4obj.select('p')
c=len(pelement)
print(c)
i=0
while i<c:
   print(str(pelement[i]))
   print(pelement[i].getText())
   print(pelement[i].attrs)
   i=i+1
file.close()
