#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



def Conncet_Web_Browers():  # Connect Web Browers
        
        ### Chrome ###
        
   
        ## 設定Chrome的瀏覽器彈出時遵照的規則
        ## 這串設定是防止瀏覽器上頭顯示「Chrome正受自動控制」
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)


        ##  設定Chrome將禁用某些彈出提示，包括"密碼太弱"提示。
        options.add_argument("--disable-infobars")

        ##  禁用擴展
        options.add_argument("--disable-extensions")

        ##  禁用彈出攔截
        options.add_argument("--disable-popup-blocking")

        ##  禁用通知
        options.add_argument("--disable-notifications")

        ##  禁用密碼儲存提示
        options.add_argument("--disable-save-password-bubble")

        ##  禁用密碼更改提示
        options.add_argument("--disable-password-change")

        ##  關閉自動記住密碼的提示彈窗
        options.add_experimental_option("prefs", {
                                        "profile.password_manager_enabled": False, "credentials_enable_service": False})

   
        # 創建一個 Chrome WebDriver 實例
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)  # 设置隐式等待时间
        driver.get("https://scr.cyc.org.tw/tp20.aspx?Module=net_booking&files=booking_before&PT=1")
        time.sleep(100)
        return driver

Conncet_Web_Browers()


