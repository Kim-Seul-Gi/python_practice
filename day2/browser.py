import webbrowser

idol = ["아이유","태연","둘리"]

for i in idol:
    webbrowser.open('https://www.google.com/search?q='+i) #+i는 i라는 문자를 더해주겠다는 의미

    
# f string = 문자열 안에 변수가 있음을 인식하게끔 한다 > webbrowser.open(f"http:www.google.com/search?q={i}")
# 여기에서i는 변수들이다.
# time.sleep(숫자) 함수는 import하고나서 실행이 가능한데, 이거는 동시에 파일이 열리면 씹힐 수 있어서
# for 루프 안에 있는 것들에 몇초간의 delay를 일부러 주는 것이다.
# requests 라는 내장함수는 요청함수?이다.
base_url = "https://www.google.com/search?q="
for member in idol:
    webbrowser.open(f"https://www.google.com/search?q={member}")
    webbrowser.open(base_url+member) # 다 같은 의미입니다.


