import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
response = requests.get(url)

#2. 원하는 정보를 찾는다.
soup = BeautifulSoup(response.text, 'html.parser')
#html 문서를 조작할 것. 받은 문서를 보기 좋게 검색하기 좋게 만들어줘

#3. Select는 CSS의 선택자(selector)를 통해 찾을 수 있다.
# #KOSPI_now : id가 KOSPI_now인 것.
# .up : class가 up인 것.
# CSS에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.
kospi = soup.select_one("#contentarea > div.box_top_submain2 > div.rgt")
#select 문서를 뽑아줘


print(kospi)
print(kospi.text)



