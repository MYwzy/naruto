"""邬宗圆的功能自动化day01任务代码"""

# 任务一：百度搜索一个东西
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("MY邬宗圆")
# driver.find_element_by_xpath('//*[@id="su"]').click()
# time.sleep(2)
# driver.quit()

# 任务二：除滑动模块，其他小任务都用自动化来做
# 表单提交
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get(r"F:/自动化测试16/练习的html/上传文件和下拉列表/autotest.html")
# driver.maximize_window()
# # 输入用户名
# driver.find_element_by_xpath("//*[@id='accountID']").send_keys("MY邬宗圆")
# driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("666666")
# driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='sexID2']").click()
# driver.find_element_by_xpath("//*[@value='spring']").click()
# driver.find_element_by_xpath("//*[@value='Auterm']").click()
# # 上传文件，
# driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\Pictures\picture.jpg")

# 弹框
# from  selenium import webdriver
# driver = webdriver.Chrome()
# driver.get(r"F:/自动化测试16/练习的html/弹框的验证/dialogs.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='confirm']").click()
# driver.switch_to.alert.accept()  # 确定
# driver.switch_to.alert.dismiss()  # 取消

# 任务三：京东搜索一个商品，点击详情
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get("https://global.jd.com/?utm_medium=cpc&utm_source=google&utm_"
#            "campaign=AmericaBrandC013&gclid=EAIaIQobChMIza66nvu58wIVrB-"
#            "tBh05WQVBEAAYASAAEgIeMvD_BwE")
# driver.maximize_window()
# driver.find_element_by_xpath('//*[@id="key"]').send_keys("华为手机")
# driver.find_element_by_xpath('//*[@id="search-link"]/i').click()