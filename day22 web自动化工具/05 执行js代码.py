import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.jd.com/')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(3)