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
# 隐式等待
chrome.implicitly_wait(10)

# 查找响应页面中的某个标签元素
search = chrome.find_element(By.ID, 'key')

# wait = WebDriverWait(chrome, 10, 0.5)
# wait.until(EC.presence_of_element_located((By.ID, "key")))

chrome.quit()