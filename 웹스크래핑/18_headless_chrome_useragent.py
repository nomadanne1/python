from selenium import webdriver

# ★ Headless 크롬
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
# 문제 해결 방법 !
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# >> 나의 user-agent
# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/90.0.4430.212 Safari/537.36

# >> headless 크롬사용시 출력 결과
# Mozilla/5.0 (Windows NT 10.0; Win64; x64)
# AppleWebKit/537.36 (KHTML, like Gecko) 
# HeadlessChrome/90.0.4430.212 Safari/537.36

# >> headless 크롬일 경우 따로 user-agent 설정 안해주면 
# HeadlessChrome 정보가 들어가기 떄문에 브라우저 접속 막힐 수 있음