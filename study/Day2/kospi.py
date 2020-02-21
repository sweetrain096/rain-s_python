import requests
from bs4 import BeautifulSoup
#import : requests의 모든 것을 가져온다.
#bs4에서 하나만 뽑아서 가져온다.

url = "https://finance.naver.com/sise/"
#1. 원하는 사이트에 요청을 보낸다.
#그리고 그 결과를 response에 저장한다.
response = requests.get(url)
#print(response.text)
#print(type(response))

#2. 원하는 정보를 찾는다.
soup = BeautifulSoup(response.text, 'html.parser')
#html 문서를 조작할 것. 받은 문서를 보기 좋게 검색하기 좋게 만들어줘

#3. Select는 CSS의 선택자(selector)를 통해 찾을 수 있다.
# #KOSPI_now : id가 KOSPI_now인 것.
# .up : class가 up인 것.
# CSS에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.
kospi = soup.select_one("#KOSPI_now")
#select 문서를 뽑아줘


print(kospi)
print(kospi.text)