import requests
from bs4 import BeautifulSoup
url = "https://www.naver.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
keyword = soup.select('.ah_roll') #    .a는 클래스 이름을 가져오기 위함, #a 는 아이디가 a인 것? 
lists=keyword[0].select('.ah_k')
for word in lists:
    print(word.text)