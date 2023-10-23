from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument("--headless")
# opt.add_argument("--window-size=1200,800")  # 设置窗口大小

chrome = webdriver.Chrome(options=opt)

# 发起请求
chrome.get('https://www.jd.com')
# time.sleep(5)
# 查找响应页面中的某个标签元素
imgs = chrome.find_elements(By.CLASS_NAME, 'focus-item-img')

for img_el in imgs:
    print(img_el.get_attribute("src"))

chrome.quit()