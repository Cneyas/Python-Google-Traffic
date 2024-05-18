import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

proxy_address = "D5f9SXMlg4-mix_sc-tr_İstanbul_istanbul:mL1pA39kiZPMK20w@gw.proxy.rainproxy.io:5959"
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy_address}')

selenium_service = Service('path_to_chromedriver')
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)

driver.get('https://www.google.com')

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('kelime')
search_box.send_keys(Keys.RETURN)

sitelink = driver.find_element(By.PARTIAL_LINK_TEXT, 'https://sitelink.com')
sitelink.click()

actions = ActionChains(driver)
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)

actions.send_keys(Keys.PAGE_UP).perform()
time.sleep(1)
actions.send_keys(Keys.PAGE_UP).perform()
time.sleep(1)
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
actions.send_keys(Keys.PAGE_DOWN).perform()
time.sleep(1)
actions.send_keys(Keys.PAGE_DOWN).perform()

driver.quit()