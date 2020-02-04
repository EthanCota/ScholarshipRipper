from Selenium import Webdriver

codeList = open('codes.txt','r', encoding='UTF8')

driver = webdriver.Chrome('C:\\chromedriver')
driver.get('http://ultimatescholarshipbook.com')

for i in range(0, 9999) #TODO Fix 9999 value to correct value
  code = codeList.readline()
  
  driver.find_element_by_name('criteria').sendKeys(code)
  deriver.find_element_by_tag_name('select').
