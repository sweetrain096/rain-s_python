import datetime
import requests
# 1. 요청 url 만들기
key = "ec4dbf0647e1f8979fd9499f080e2edb"
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
today = datetime.datetime.today()
sevendaysago_date = f"{today.year}{today.month}{today.day-7}"
print(sevendaysago_date)
week_url = f"{url}?key={key}&targetDt={sevendaysago_date}"
ko_url = f"{url}?key={key}&targetDt={sevendaysago_date}&repNationCd=K"
national_url = f"{url}?key={key}&targetDt={sevendaysago_date}&repNationCd=F"

# 2. 요청

response = requests.get(ko_url).json()
weeklyBoxOfficeList = response['boxOfficeResult']['weeklyBoxOfficeList']
total = len(weeklyBoxOfficeList)
print("한국 영화 순위")
for i in range(total) :
    print(i+1, weeklyBoxOfficeList[i]['movieNm'])


response = requests.get(national_url).json()
weeklyBoxOfficeList = response['boxOfficeResult']['weeklyBoxOfficeList']
total = len(weeklyBoxOfficeList)
print("\n외국 영화 순위")
for i in range(total) :
    print(i+1, weeklyBoxOfficeList[i]['movieNm'])

