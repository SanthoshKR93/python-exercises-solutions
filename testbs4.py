import bs4,requests
file=open('myfile.html')
bs4object=bs4.BeautifulSoup(file)
elem=bs4object.select('#author')
print(len(elem))
print(str(elem))
print(elem[0].getText())
print(elem[0].get('id'))
print(elem[0].attrs)
file.close()