import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException
from selenium.webdriver.common.by import By
# 很多网页中存在 frame 标签，要处理frame里面的数据，首先要切入frame，处理完了还要切出来。
# 切入用switch_to.frame，切出用switch_to.parent_frame

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')  # 进入frame   iframeResult是iframe的id
source = browser.find_element(By.CSS_SELECTOR,'#draggable')
browser.switch_to.parent_frame() # 退出frame


