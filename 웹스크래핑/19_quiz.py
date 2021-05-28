# Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # Key.ENTER

browser = webdriver.Chrome()

url = "http://daum.net"
browser.get(url)

elem = browser.find_element_by_id("q")
elem.send_keys("송파 헬리오시티")
elem.send_keys(Keys.ENTER)

soup = BeautifulSoup(browser.page_source, "lxml")

data_rows = soup.find("table", attrs={"class":"tb1"}).find("tbody").find_all("tr")

for index, row in data_rows:
    columns = row.find_all("td")
    
    print("============= 매물 {} =============".foramt(index+1))
    print("거래 :", columns[0].get_text())
    print("면적 :", columns[1].get_text(), "(공급/전용)")
    print("가격 :", columns[2].get_text(), "(만원)")
    print("동 :", columns[3].get_text())
    print("층 :", columns[4].get_text())


