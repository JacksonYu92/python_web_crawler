from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time
chrome = webdriver.Chrome()

# 发起请求
chrome.get('https://www.jd.com')
# time.sleep(5)
# 查找响应页面中的某个标签元素
search = chrome.find_element(By.ID, 'key')
search.send_keys('apple watch')
time.sleep(1)
search.clear()

search.send_keys('apple pencil')
time.sleep(1)
# search.send_keys(Keys.ENTER)
button = chrome.find_element(By.CLASS_NAME, "button")
button.click()
time.sleep(5)

chrome.quit()