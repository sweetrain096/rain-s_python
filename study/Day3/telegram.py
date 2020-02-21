import requests
import os
#환경변수에 저장해놓은 token값을 가져올것


#!!!!!!!!!!!!!!!!! 토큰은 비밀번호와 같다 !!!!!!!!!!!!
token = os.getenv("TELEGRAM_TOKEN")

url = f"https://api.telegram.org/bot{token}/getUpdates"
print(url)
#getUpdates
# 1. 요청을 보내자. (id값) 보낸 결과를 response 변수에 저장.
# 결과가 JSON이면 BeautifulSoup 을 사용하지 않아도 된다.

response = requests.get(url)
#print(response)


# 2. json 형식으로 바꾼다.
# 지금은 dictionary와 list가 섞여있는것과 같다고 생각해도 된다.
updates = response.json()
#print(updates)
#print("")

# 3. user의 id를 찾는다.
user_id = updates['result'][0]['message']['from']['id']
print(user_id)




# 4. 메시지를 설정한다.
#msg = "ㅎㅎㅎㅎㅎ"
msg = input("보낼 메시지를 입력해주세요 : ")

url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"


requests.get(url)

# user_id = "663200714"
# msg = "안녕??"
# url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"
# print(url)


# #5. 메세지를 보낸다.




# Connectless
# Stateless
# 요청을 보내기만한다.
