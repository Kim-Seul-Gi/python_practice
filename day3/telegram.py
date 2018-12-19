import requests
import os
#인터넷에 URL에 나타낸 형식이 json 형식인 것이다.

# token = "4g654g65sds6gsgdgsd654dsg" #관리 잘 , 토큰은 비밀번호
# token에 나온 708449328이 봇의 id이다.
# token은 숨겨야 하므로 컴퓨터 내에 저장시키기 위해서 os 라는 환경변수를 이용한다
# export TELEGAM_TOKEN=skdljfklsdjf 해서 한 다음에
# 아래의 코드로 불러올 수 있다.
token = os.getenv("TELEGRAM_TOKEN")

# # 1. 봇의 정보 보는 방법


# url = f"https://api.telegram.org/bot{token}/getMe"

# print(url) # git bash에 나온 url를 인터넷에 복사하여 접속하면, 봇의 정보가 나온다.



# # 2. 봇을 통해 메세지를 전달하는 방법


# url = f"https://api.telegram.org/bot{token}/getUpdate" # 요청을 보낸다.

# user_id = "767810824" # 안녕안녕이라는 말을 봇에서 보내기 위해서는 아래를 이용해서 가능하다.

# msg = "안녕안녕?"

# url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"

# print(url) # git bash에 나온 url를 인터넷에 복사하여 접속하면, msg가 767810824(나)에게 전송된다.



# 3 연습 문제 

 
url = f"https://api.telegram.org/bot{token}/getUpdates"

# 3-1. 요청을 보낸 결과를 response라는 변수에 저장한다. 
response = requests.get(url)
print(url)
# 3-2. json 형식으로 바꾼다. 
updates = response.json() # json 형식으로 바뀐, 딕셔너리 형태의 updates를 정의하였다.
# 이 때의 updates는 dictionary와 list가 섞여 있는 것과 같다고 생각한다.
# print(updates)를 하면 updates의 딕셔너리 데이터가 아주 많이 나온다. 
# 그러므로 이 데이터 중에서 user_id를 찾아내야 한다. 


# 3-3. user의 id를 찾는다.
user_id = updates["result"][0]["message"]["from"]["id"]
#updates["a"] = updates 안에 있는 것 중에서 "a" 라는 key 이름을 가진 딕셔너리의 value를 가져온다.

# result라는 key의 value 값을 가져와야 한다. 
# 이 때의 value는 list 형태이다. 그리고 list의 첫 번째 값을 가져와야 하므로 [0]을 넣는다.
# [0]을 통해서 list 중에서 message라는 key의 value를 가져오고, 딕셔너리 형태에서는
# 그 중에서 from, from 중에서 id의 value를 가져올 수 있다.



# 3-4. 메시지를 설정한다.
msg = "안녕안녕?"
url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"

# 3-5. 메세지를 보낸다. 보내는 것만 한 것이기 때문에 reponse로 저장할 필요까지는 없다.
requests.get(url)

