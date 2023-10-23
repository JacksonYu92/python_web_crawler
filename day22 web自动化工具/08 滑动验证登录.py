import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import cv2

from urllib import request
from selenium.webdriver.common.action_chains import ActionChains
import sys

def get_distance():
    background = cv2.imread("background.png", 0)
    gap = cv2.imread("gap.png", 0)

    res = cv2.matchTemplate(background, gap, cv2.TM_CCOEFF_NORMED)
    # print("res:::", res)
    value = cv2.minMaxLoc(res)[2][0]
    print("value:::",value)
    # sys.exit()
    return value * 242 / 360


def main():
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(5)

    chrome.get('https://passport.jd.com/new/login.aspx?')

    # login = chrome.find_element(By.CLASS_NAME, 'login-tab-r')
    # login.click()

    loginname = chrome.find_element(By.ID, 'loginname')
    loginname.send_keys("123@qq.com")

    nloginpwd = chrome.find_element(By.ID, 'nloginpwd')
    nloginpwd.send_keys("987654321")

    loginBtn = chrome.find_element(By.CLASS_NAME, 'login-btn')
    loginBtn.click()

    # 下载图片
    background_src = chrome.find_element(By.XPATH, '//*[@class="JDJRV-bigimg"]/img').get_attribute("src")
    gap_src = chrome.find_element(By.XPATH, '//*[@class="JDJRV-smallimg"]/img').get_attribute("src")

    request.urlretrieve(background_src, "background.png")
    request.urlretrieve(gap_src, "gap.png")

    # 计算滑动距离
    distance = get_distance()
    print("distance", distance)

    print('第一步,点击滑动按钮')
    element = chrome.find_element(By.CLASS_NAME, 'JDJRV-slide-btn')
    ActionChains(chrome).click_and_hold(on_element=element).perform()  # 点击鼠标左键，按住不放

    ActionChains(chrome).move_by_offset(xoffset=distance, yoffset=0).perform()
    ActionChains(chrome).release(on_element=element).perform()
    time.sleep(5)

if __name__ == '__main__':
    main()