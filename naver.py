import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
response = requests.get(url)

#2. 원하는 정보를 찾는다.
soup = BeautifulSoup(response.text, 'html.parser')
#html 문서를 조작할 것. 받은 문서를 보기 좋게 검색하기 좋게 만들어줘

#3. Select는 CSS의 선택자(selector)를 통해 찾을 수 있다.
# #KOSPI_now : id가 KOSPI_now인 것.
# .up : class가 up인 것.
# CSS에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.

key = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base")
#key = soup.select_one(".ah_roll")

keys = key.select(".ah_k")
print(len(keys))
i = 0
for i in range (len(keys)):
    
    key_word = keys[i]
    
    print(key_word.text)
    