# # url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=400"
# # url 에서 method 는 요청변수, & 다음에 drwNo 도 요청변수이다.
import requests

# # 0. 요청 url 만들기
key = "906406d2820a6e6bbd351c1cb5fd4832"
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"

url = f"{url}?key={key}&targetDt=20181215"

# # 1. 요청
response = requests.get(url).json()
movie_list=response["boxOfficeResult"]["dailyBoxOfficeList"][2]["movieNm"]
# # print(movie_list)
# # print(type(movie_list)) # string


# 1. 요청
print(url)
movie_list=[]
for i in list(range(0,10)):
    movie_list.append(response["boxOfficeResult"]["dailyBoxOfficeList"][i]["movieNm"])

print(movie_list)
#f-string 에 대해서 알아야 할 것 같다.

# a=[]
# for i in list(range(0,10)):
#     a.append(f"{i}")
# print(a)
