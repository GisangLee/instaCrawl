from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
print("라이브러리 임포트 완료".rjust(20, '-'))


base_url = "https://www.instagram.com/explore/tags/"
plus_url = input("검색할 태그를 입력하세요:  ")

url = base_url + quote_plus(plus_url)

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select(".v1Nh3.kIKUG._bz0w")

imgnum = 1
for i in insta:
    print('https://www.instagram.com' + i.a['href'])
    Img_Url = i.select_one('.KL4Bh').img['src']

    with urlopen(Img_Url) as f:
        with open(plus_url + str(imgnum) + '.jpg', 'wb') as file_name:
            img = f.read()
            file_name.write(img)

    imgnum += 1

print("사진 다운로드 완료".rjust(20, '-'))

driver.close()

