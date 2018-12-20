import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(url)
#print(response.text)
#2. 원하는 정보를 찾는다.
soup = BeautifulSoup(response.text, 'html.parser')
#html 문서를 조작할 것. 받은 문서를 보기 좋게 검색하기 좋게 만들어줘

#3. Select는 CSS의 선택자(selector)를 통해 찾을 수 있다.
# #KOSPI_now : id가 KOSPI_now인 것.
# .up : class가 up인 것.
# CSS에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.
#print(soup)

key = soup.select(".tit")
#key = soup.select(".href")
#print(key)

#key = soup.select_one(".ah_roll")

#keys = key.select(".a")
# print(len(keys))
# i = 0
# for i in range (len(keys)):
    
#     key_word = keys[i]
    
#     print(key_word.text)
    
#print(key[0]
num = 1

# for i in key[0] :
#     print(num, i)
#     num += 1

# print(key[0].select(a))

print(type(key[0]))
#print(key[0])