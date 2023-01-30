from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(service=Service(chrome_driver_path))

url = "https://tinder.com/"
driver.get(url=url)
driver.maximize_window()
time.sleep(2)
main_window_handle = None

while not main_window_handle:
    main_window_handle = driver.current_window_handle

accept_button = driver.find_element(by=By.XPATH, value='//*[@id="q-401777178"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()
time.sleep(2)

button_log = driver.find_element(by=By.XPATH,
                                 value='//*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
button_log.click()
time.sleep(2)
button_log_with_fb = driver.find_element(by=By.XPATH,
                                         value='//*[@id="q-2130158254"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
button_log_with_fb.click()
time.sleep(4)
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to.window(signin_window_handle)

# accept_button = driver.find_element(by=By.XPATH, value='//*[@id="u_0_a_Mg"]')
# accept_button.click()
# time.sleep(2)
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("your email here")
time.sleep(2)
passw = driver.find_element(by=By.NAME, value="pass")
passw.send_keys("your password here")
passw.submit()
time.sleep(15)
driver.switch_to.window(main_window_handle)
accept_button = driver.find_element(by=By.XPATH, value='//*[@id="q-2130158254"]/main/div/div/div/div[3]/button[1]')
accept_button.click()
time.sleep(2)
accept_button = driver.find_element(by=By.XPATH, value='//*[@id="q-2130158254"]/main/div/div/div/div[3]/button[2]')
accept_button.click()
time.sleep(2)
# accept_cokkies = driver.find_element(by=By.XPATH,
#                                      value='//*[@id="q-401777178"]/div/div[2]/div/div/div[1]/div[1]/button')
# accept_cokkies.click()
# time.sleep(2)
accept_button = driver.find_element(by=By.XPATH, value='//*[@id="q-2130158254"]/main/div/div[2]/button')
accept_button.click()
time.sleep(5)

for _ in range(100):
    try:
        button_like = driver.find_element(By.XPATH,
                                          '//*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        button_like.click()
        # disslike_button = driver.find_element(By.LINK_TEXT,
        #                                       '//*[@id="q-401777178"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
        # disslike_button.click()

    except NoSuchElementException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)
    time.sleep(5)
    driver.quit()
