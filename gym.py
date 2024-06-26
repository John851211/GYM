#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime, timedelta


URL2 ="https://scr.cyc.org.tw/tp20.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1&D=2024/06/11&D2=3"


def Conncet_Web_Browers(): #瀏覽器條件設定 

   
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
        return driver




def wait_until_noon():  #等待到午夜12點
    now = datetime.now()
    target_time = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if now.minute >= 0:
        target_time += timedelta(days=1)
    wait_time = (target_time - now).total_seconds()
    time.sleep(wait_time)





def connect_to_website_in_new_tab(driver): #開新分頁連到確認預約資訊
    # 打开一个新的空白标签页
    driver.execute_script("window.open('about:blank', '_blank');")
    # 获取当前窗口句柄
    current_window_handle = driver.current_window_handle
    # 切换到新打开的标签页
    for handle in driver.window_handles:
        if handle != current_window_handle:
            driver.switch_to.window(handle)
            break
    # 在新标签页中连接到指定的网站
    driver.get(URL2)


def select_time(driver):
     YuB = driver.find_element(By.XPATH,"/html/body/table[1]/tbody/tr[3]/td/div/form/table/tbody/tr/td/span/div/table/tbody/tr[2]/td/span/table/tbody/tr[5]/td[3]/img")
     YuB.click()   



def handle_alert(driver):
    # 處理弹出窗口
    try:
        alert = driver.switch_to.alert
        print(f"弹出窗口内容: {alert.text}")
        alert.accept()
        print("弹出窗口已关闭")
       
    except:
        print("没有检测到弹出窗口")
     





driver = Conncet_Web_Browers()
wait_until_noon()
connect_to_website_in_new_tab(driver)
select_time(driver)
handle_alert(driver)
time.sleep(100)