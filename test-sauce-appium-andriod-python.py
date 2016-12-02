# Android environment
import os
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from sauceclient import SauceClient

username = os.environ['SAUCEUSER']
accessKey = os.environ['SAUCEAPIKEY']

sauce_client = SauceClient(username,accessKey)

desired_caps = {}
desired_caps['browserName'] = 'Browser'
desired_caps['appiumVersion'] = '1.4.16'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['name'] = 'Sample Test2'

url = 'http://' + username + ':' + accessKey + '@ondemand.saucelabs.com:80/wd/hub'

driver = webdriver.Remote(url, desired_caps)

driver.get('http://www.testamy.com')
sleep(3)
contexts = driver.contexts
driver.switch_to.context(contexts[-1])

elem = driver.find_element_by_class_name('next')
elem.click()
actual = driver.find_element_by_class_name('current').text
expected = '2'

if (actual == expected):
    sauce_client.jobs.update_job(driver.session_id, passed=True)
else:
    sauce_client.jobs.update_job(driver.session_id, passed=False)


driver.quit()

