import os
import requests
import datetime
import csv

key = os.getenv("KOBIS_KEY")
kobis_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
targetDt = datetime.datetime(2019, 1, 13)
targetDt -= datetime.timedelta(days=70)
movie_list =[]

for week in range(10):
    targetDt += datetime.timedelta(days=7)
    targetDt_str = targetDt.strftime("%Y%m%d")
    # f"{targetDt.year}{targetDt.month}{targetDt.day-(7*week)}"
    print(targetDt_str)

    response = requests.get(f"{kobis_url}?key={key}&targetDt={targetDt_str}&weekGb=0").json()
    # print(f"{kobis_url}?key={key}&targetDt={20190113}&weekGb=0")

    for rank in range(0, 10):
        now_content = response["boxOfficeResult"]["weeklyBoxOfficeList"][rank]
        now_dict = {
            "영화코드" : now_content["movieCd"],
            "영화명" : now_content["movieNm"],
            "해당일누적관객수" : now_content["audiCnt"],
            "해당일" : targetDt_str
        }
        movie_list.append(now_dict)
        # if not now_dict["영화코드"] in movie_list[:]["영화코드"]:
        #     movie_list.append(now_dict)
        # print(now_content["movieNm"])

print(movie_list)
print(movie_list[0]["영화코드"])


# with open("boxoffice.csv", "w", encoding="utf-8", newline="") as f:
#     fieldnames = ["영화코드", "영화명", "해당일누적관객수", "해당일"]
#     write = csv.DictWriter(f, fieldnames=fieldnames)
#     write.writeheader()
#     for movie in movie_list:
#         write.writerow(movie)