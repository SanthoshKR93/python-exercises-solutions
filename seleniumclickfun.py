from selenium import webdriver
browser=webdriver.Firefox(executable_path=r'/home/killbox/Downloads/geckodriver')
browser.get('http://inventwithpython.com')
try:
   elemobj=browser.find_element_by_link_text('Coding with Minecraft')
   elemobj.click()
except:
   print('no such line')
