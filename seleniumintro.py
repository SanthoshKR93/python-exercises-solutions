from selenium import webdriver   #from selenium module, webdriver sub module is loaded
browser=webdriver.Firefox(executable_path=r'/home/killbox/Downloads/geckodriver')   #opens up firefox browser
browser.get('https://www.google.com')
