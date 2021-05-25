import requests
import re
from bs4 import BeautifulSoup

# 아이디어스 파우치 리뷰 스크래핑

for p in range(1, 60):
    url = "https://www.idus.com/w/product/b82732ce-2762-48b5-9879-e0d5838d5fc3?keyword_channel=user&search_word=+%EB%8B%AC%EC%9D%B4%EC%9E%88%EB%8A%94%EB%B0%A4&review_page={}".format(p)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    reviews = soup.find_all("li", attrs={"class":"review-contents"})

    for review in reviews:
        content = review.get_text()

        if "로지텍" in content:
            print(content)
            # print("#"*20)
