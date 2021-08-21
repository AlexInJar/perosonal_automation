from selenium import webdriver
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_argument("--headless")
browser = webdriver.Chrome(options = opts)
browser.get('http://www.baidu.com/')
print(browser.page_source)
browser.close()
