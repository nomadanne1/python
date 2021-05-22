from selenium import webdriver

browser = webdriver.Chrome() # 다른경로에 있을경우 명시 ex) .Chrome("c://downloads/chromdriver.exe")
browser.get("http://naver.com")

# # find_element_by_class_name("")
# elem = browser.find_element_by_class_name("link_login")
# elem.click()

# browser.back()
# browser.forward()
# browser.refresh()

# # .find_element_by_id("") , 나도 코딩 검색
# elem = browser.find_element_by_id("query")
from selenium.webdriver.common.keys import Keys # Key.ENTER
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

elem = browser.find_element_by_tag_name("a")
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    e.get_attribute("href") # cf. BeautifulSoup ["href"]

browser.get("https://daum.net")
elem =  browser.find_element_by_name("q")
elem.send_keys("나도코딩") 
elem.send_keys(Keys.ENTER)  
browser.back()
elem =  browser.find_element_by_name("q") # *페이지 전환시 elem 다시 세팅해줘야함.

# XPATH
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")

