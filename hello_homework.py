from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload


# 1. 환경 설정-드라이버 경로  
chrome_drive_path = "C:/Users/ShipJobs/googledriverpath/chromedriver.exe"  

driver = webdriver.Chrome(chrome_drive_path) # 웹드라이버 파일의 경로


driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%B9%B4%EB%8B%88%EB%B0%9C+%ED%92%80%EC%B2%B4%EC%9D%B8%EC%A7%80")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

#select_one
#select

##_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(2) > a.thumb._thumb > img
#thumnnails = soup.select('##_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div > a.thumb._thumb > img') #img 테크 전체
"""
thumnnails = soup.select_one('#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb > img')['src']
print(thumnnails)
"""

thumnnails = soup.select('#_sau_imageTab > div > div > div > a > img') #img 테크 전체
i = 1 
for thumnnail in thumnnails:
    image_URL = thumnnail['src']
    
    print(image_URL)
    dload.save(image_URL ,f'car_img/{i}.jpg')  #폴더가 경로에 위치 해야 함
    i += 1

driver.quit() # 끝나면 닫아주기