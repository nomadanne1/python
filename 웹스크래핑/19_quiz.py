# Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res= requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"tb1"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows): # enumerate(data_row)
    columns = row.find_all("td")
    
    print("============= 매물 {} =============".format(index+1))
    print("거래 :", columns[0].get_text().strip())
    print("면적 :", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 :", columns[2].get_text().strip(), "(만원)")
    print("동 :", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())

# >> 'NoneType' object has no attribute 'find' 오류 발생.