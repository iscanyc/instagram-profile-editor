from selenium import webdriver
import time

driver_path = "C:\PyProjects\selenium\chromedriver.exe"

# proxy = "http://ip:port"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % proxy)
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--ignore-ssl-errors')

UserName = ""
Password = ""

browser = webdriver.Chrome(driver_path)
browser.get("http://www.instagram.com/")
time.sleep(10)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
login = browser.find_element_by_tag_name("button")
username.send_keys(UserName)
password.send_keys(Password)
login.click()
time.sleep(5)
browser.get("https://www.instagram.com/" + UserName)
time.sleep(5)
edit = browser.find_elements_by_tag_name("button")
edit[1].click()
time.sleep(5)
url = browser.find_element_by_id("pepWebsite")
url.send_keys("https://randmovie.com")
save = browser.find_elements_by_tag_name("button")[2]
save.submit()
time.sleep(5)
browser.quit()
