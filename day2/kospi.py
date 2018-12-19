#코스피 지수를 크롤링하는 것.

import requests
from bs4 import BeautifulSoup #bs4라는 모듈중에 beau~만 가져오겠다는 의미.

url = "https://finance.naver.com/sise/" 
response = requests.get(url) # 원하는 사이트에 요청을 보낸다. 그리고 결과를 response에 저장한다.
#print(response.text)
#print(type(response)) #우리가 요청한 소스코드가 와 있는 것이다.

#원하는 정보를 찾는 방법
soup = BeautifulSoup(response.text, 'html.parser') #구문을 가져와서 조작할 것이다.
kospi = soup.select_one('#KOSPI_now') #무엇을 찾을건지.우클릭>검사>구문에 우클릭 copy>copy selector  후 복사
# 이를 통해 select는 CSS의 선택자(selector)를 통해 찾을 수 있다.
# #KOSPI_now : id 가 KOSPI_NOW인 것.
# .up : class 가 up인 것.
# CSS에서 id는 문서에서 하나, class는 여러개가 있을 수 있다.
 
print(kospi.text)

#beautifulSoup 는 컴퓨터가 잘 찾기위해 데이터 type을 바꿔놓는 것이라고 생각하면 편하다.


