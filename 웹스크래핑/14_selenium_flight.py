from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url 이동

# 가는날 선택 클릭 
browser.find_element_by_link_text("가는날 선택").click()

# # 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번달

# # 다음날 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 이번달 27일, 다을달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()


# 첫 번째 결과 출력 *loding시간으로 인해 오류 발생.
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)

# ★loding시간으로 인한 오류 해결 ex) no such element
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
# 1. WebDriverWait를 통해서 브라우저 (최대)10초동안 기다린다.
# 2. EC.presence_of_element_located ~> By.XPATH라는 조건으로 해당하는 엘리먼트가 위치할때까지.
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) # ※괄호2개 
    # 성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()