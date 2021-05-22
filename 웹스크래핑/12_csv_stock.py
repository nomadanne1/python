import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline="" - 자동줄바꿈없앰, "utf-8-sig" - 엑셀파일 열때 한글깨질때
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") 
# ["N", "종목명", "현재가", ...] - str.split() : 문자열 -> list
print(type(title))
writer.writerow(title)

# 코스피 시가총액 상위  1 ~ 200
for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns)  <= 1: # 의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns] # 한줄 for문 [list], *strip() - 문자열에서 양쪽에 있는 연속된 모든 공백 삭제.
        # print(data)
        writer.writerow(data)

