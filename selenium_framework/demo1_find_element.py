from selenium import webdriver
from selenium.webdriver.common.by import By

# 构造模拟浏览器
# ie_login = webdriver.Ie()
# firefox_login = webdriver.Firefox()
# chrome_login = webdriver.Chrome()



# 可设定无界面模式，即操作浏览器时，隐层浏览器
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 设置无界面  可选
chrome_login = webdriver.Chrome(chrome_options=options)


# 访问页面
chrome_login.get('http://www.baidu.com/')
# chrome_login.maximize_window() # 窗口最大化
chrome_login.minimize_window()   # 窗口最小化


# 单元素查找并交互
input = chrome_login.find_element(By.ID, "q")
input_clear = input.clear()
input.send_keys("query")


name = chrome_login.find_element(By.NAME)
xpath = chrome_login.find_element(By.XPATH)
link_text = chrome_login.find_element(By.LINK_TEXT)
partial_link_text = chrome_login.find_element(By.PARTIAL_LINK_TEXT)
tag_name = chrome_login.find_element(By.TAG_NAME)
class_name = chrome_login.find_element(By.CLASS_NAME)
css_selector = chrome_login.find_element(By.CSS_SELECTOR)
## 下面的方法在新版中遗弃
# chrome_login.find_element_by_id('email').clear()
# chrome_login.find_element_by_id("email").send_keys("rocket_2014@126.com")
# chrome_login.find_element_by_name()
# chrome_login.find_element_by_xpath()
# chrome_login.find_element_by_link_text()
# chrome_login.find_element_by_partial_link_text()
# chrome_login.find_element_by_tag_name()
# chrome_login.find_element_by_class_name()
# chrome_login.find_element_by_css_selector()

# 多元素查找
chrome_login.find_elements()






# 获取文本 logo.text
#
# 获取id logo.id
#
# 获取位置 logo.location
#
# 获取标签名logo.tag_name
#
# 获取size logo.size









# title_is：判断当前页面的title是否等于预期
# title_contains：判断当前页面的title是否包含预期字符串
# presence_of_element_located：判断某个元素是否被加到了dom树里，并不代表该元素一定可见
# visibility_of_element_located：判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
# visibility_of：跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
# presence_of_all_elements_located：判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
# text_to_be_present_in_element：判断某个元素中的text是否 包含 了预期的字符串
# text_to_be_present_in_element_value：判断某个元素中的value属性是否包含了预期的字符串
# frame_to_be_available_and_switch_to_it：判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
# invisibility_of_element_located：判断某个元素中是否不存在于dom树或不可见
# element_to_be_clickable - it is Displayed and Enabled：判断某个元素中是否可见并且是enable的，这样的话才叫clickable
# staleness_of：等某个元素从dom树中移除，注意，这个方法也是返回True或False
# element_to_be_selected：判断某个元素是否被选中了,一般用在下拉列表
# element_located_to_be_selected
# element_selection_state_to_be：判断某个元素的选中状态是否符合预期
# element_located_selection_state_to_be：跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
# alert_is_present：判断页面上是否存在alert
