#%%e
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from helper.source_env import conf_source

inno_username,inno_password = conf_source('inno_username','inno_password')
#%%

# set timer



def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        print(f"{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Countdown completed!")


while True:
    COUNTDOWN = input("input the countdown in minutes: ")

    if COUNTDOWN.isnumeric():
        COUNTDOWN = int(COUNTDOWN)
        break


countdown(COUNTDOWN)

while True:
    try:
        browser = webdriver.Firefox()
        # browser.get('https://internal.innovatureinc.com/web?db=innovatureinc&token=UVdeayxvWUOWxJmMBhow#action=364&cids=1&menu_id=240')
        browser.get('https://internal.innovatureinc.com/web#action=364&cids=1&menu_id=240')
        user_name = browser.find_element(By.ID,'login')
        pass_word = browser.find_element(By.ID,'password')
        user_name.send_keys(inno_username)
        pass_word.send_keys(inno_password)
        browser.find_element(By.XPATH, "//*[contains(text(), 'Log in')]").click()





        # # click the button
        #wait for login
        time.sleep(20)
        checkout_button_css = ".fa.fa-7x.o_hr_attendance_sign_in_out_icon.fa-sign-out.btn-warning"
        browser.find_element(By.CSS_SELECTOR, checkout_button_css).click()
    except Exception as e:
        continue
    else:
        break