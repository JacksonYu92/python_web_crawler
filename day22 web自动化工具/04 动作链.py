from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://sahitest.com/demo/dragDropMooTools.htm')

dragger = driver.find_element(By.ID, 'dragger')  # 被拖拽元素
item1 = driver.find_element(By.XPATH, '//div[text()="Item 1"]')  # 目标元素1
item2 = driver.find_element(By.XPATH, '//div[text()="Item 2"]')  # 目标2
item3 = driver.find_element(By.XPATH, '//div[text()="Item 3"]')  # 目标3
item4 = driver.find_element(By.XPATH, '//div[text()="Item 4"]')  # 目标4
action = ActionChains(driver)
action.drag_and_drop(dragger, item1).perform()  # 1.移动dragger到目标1
sleep(2)
action.click_and_hold(dragger).release(item2).perform()  # 2.效果与上句相同，也能起到移动效果
sleep(2)
action.click_and_hold(dragger).move_to_element(item3).release().perform()  # 3.效果与上两句相同，也能起到移动的效果
sleep(2)
action.click_and_hold(dragger).move_by_offset(800, 0).release().perform()
sleep(2)
driver.quit()