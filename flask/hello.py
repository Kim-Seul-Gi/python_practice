from flask import Flask, render_template #flask라는 것을 통해서 웹서버를 돌려놓은 상태이다.
#render_template은 따로임 ㅇㅇ
import datetime
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

# $ FLASK_APP=hello.py flask run 를 하면 http 주소가 나오고
# 그 주소로 인터넷에서 복붙을 하면 hello world 가 나오는 웹이 나온다. cntl+c가 프로그램 강제종료 로 탈출

@app.route("/ssafy")
def saffy():
    return "안녕 싸피~"

@app.route("/isitchristmas")
def christmas():
    now = datetime.datetime.today()
    day=now.day
    month=now.month
    year=now.year
    if day==25 and month ==12:
        return "예"
    else:
        return "아니오" #이러한 결과를 웹이 뿌릴 수 있는 상태인 것이다.
        # py 파일 저장하고 $ FLASK_APP=hello.py flask run 로 실행 후 url 들어가면 된다.


@app.route("/greeting/<string:name>") #변수로 url를 설정
def greeting(name): #name을 인자로 넘겨줘야 한다.
    return f"{name}야 안녕"


@app.route("/cube/<int:num>") 
def cube(num):
    return f"부피는 {num**3}입니다."   # python에서는 a^b는 승 이 아니라 XOR 이다.
    # a**b 는 a의 b 승이다.

@app.route("/dinner") # 저녁 리스트를 만들고 그 중에서 하나를 뽑는다.
def dinner():
    dinner = ["짜장면","피자","비빔밥","빵","라면","치킨","떡볶이"]
    menu = random.choice(dinner)
    return render_template("dinner.html", menu=menu, dinner=dinner)

@app.route("/drama") 
def drama():
    drama = ["뷰티인사이드","그냥 자라"]
    
    # 나는 html 파일 자체에 해당 드라마가 나오면 이미지가 나오게 만들었는데, py 파일에서 for문을 넣어서 이미지를 적용시킬 수 있다. 아래가 그 예이다.
    image_urls = {
        "뷰티인사이드" : "http://fs.jtbc.joins.com/prog/drama/beautyinside/Img/site/Main/20181121092247.jpg",
        "그냥 자라" : "https://cbmpress.com/toronto/wp-content/uploads/sites/3/2018/01/y.jpg"
    }
    # 그 중 하나를 뽑는 것을 만든다.
    pick = random.choice(drama)
    pick_url = image_urls[pick]
    return render_template("drama.html", pick=pick, drama=drama, pick_url=pick_url)