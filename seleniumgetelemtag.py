from selenium import webdriver
browser=webdriver.Firefox(executable_path=r'/home/killbox/Downloads/geckodriver')
browser.get('http://inventwithpython.com')
try:
   elemobj=browser.find_element_by_class_name('card')
   print('tag found is <%s>' % (elemobj.tag_name))
except:
   print('no such line')
