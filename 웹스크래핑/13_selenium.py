import time 
from selenium import webdriver

browser = webdriver.Chrome() # 다른경로에 있을경우 명시 ex) .Chrome("c://downloads/chromdriver.exe")

# 1. 네이버로 이동
browser.get("http://naver.com")

# # find_element_by_class_name("")
elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.back()
browser.forward()
browser.refresh()

# .find_element_by_id (나도 코딩 검색)
elem = browser.find_element_by_id("query")
from selenium.webdriver.common.keys import Keys # Key.ENTER
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

# .find_element_by_tag_name
elem = browser.find_element_by_tag_name("a")
elem = browser.find_elements_by_tag_name("a")
for e in elem:
    e.get_attribute("href") # cf. BeautifulSoup ["href"]

# .find_element_by_name
browser.get("https://daum.net")
elem =  browser.find_element_by_name("q")
elem.send_keys("나도코딩") 
elem.send_keys(Keys.ENTER)  
browser.back()
elem =  browser.find_element_by_name("q") # *페이지 전환시 elem 다시 세팅해줘야함.

# .find_element_by_xpath (XPATH)
elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3) # import time

# 5. id 를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료
