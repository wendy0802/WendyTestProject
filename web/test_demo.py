import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        db = shelve.open("cookies")
        # Step 1. 在登录状态下保存cookie
        # db['cookies'] = self.driver.get_cookies()

        # Step 2. 使用db里面保存的cookie登录企业微信
        cookies = db['cookies']
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.ID, 'menu_contacts').click()
        sleep(5)
        db.close()
