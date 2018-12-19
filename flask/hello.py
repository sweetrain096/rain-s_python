from flask import Flask, render_template #모듈 불러오기
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)   #flask 만들기

@app.route("/")     #경로 설정
def hello():
    return render_template("index.html")

@app.route("/ssafy")     #경로 설정
def ssafy():
    return "ssafy중입니다~!"
today = f"{datetime.today().month}.{datetime.today().day}"
print(today)
@app.route("/isitchristmas")
def christmas():
    if today == "12.25" :
        return "네!"
    else :
        return "아니오"

#variable routing
#url의 값들이 서버에서는 변수로 사용. 그 값을 가지고 와서 함수의 인자로 넘겨준다.
@app.route("/greeting/<string:name>")
def greeting(name):
    return f"{name} 안녕~"

@app.route("/cube/<int:num>")
def cube(num) :
    return f"{num**3}"

@app.route("/dinner")
def dinner() :
    # 1. 저녁 list 만들고
    menus = ["치맥", "해물찜", "초밥"]
    img_url = {
        "치맥" :"http://dimg.donga.com/i/660/0/90/ugc/CDB/SODA/Article/59/00/42/4b/5900424b022bd2738de6.jpg",
        "해물찜" : "http://recipe1.ezmember.co.kr/cache/recipe/2018/03/29/6977b9fd7cc20e915c2c9036c93999b21.jpg",
        "초밥" : "https://resources.matcha-jp.com/old_thumbnails/720x2000/1529.jpg"
    }

    # 2. 하나 뽑기
    menu = random.choice(menus)
    menus_url = img_url[menu]

    return render_template("dinner.html", menu=menu, dinner = menus, menus_url = menus_url)
    # 파란글씨 :dinner.html에서 사용, 흰 menu는 여기서 사용되는 변수


# @app.route("/movie")
# def movie():
#     url = "https://movie.naver.com/movie/running/current.nhn"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     key = soup.select("#content > div.article > div:nth-child(1) > div.lst_wrap")

#     return f"{key}"

    

