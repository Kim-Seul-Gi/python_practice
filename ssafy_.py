'''
ssafy.txt
안녕
하세요
저는
김탁희
입니다
만나서
반갑습니다

>ssafy.txt 역순으로 result.txt에 저장을 해주세요
'''

# with open("ssafy.txt","w") as file:
#     file.write("안녕\n")
#     file.write("하세요\n")
#     file.write("저는\n")
#     file.write("김탁희\n")
#     file.write("입니다\n")
#     file.write("만나서\n")
#     file.write("반갑습니다\n")


with open("ssafy.txt","r") as file:
    words = file.readlines()

r_words = reversed(words)

with open("result.txt","w") as file:
    for line in r_words:
        file.write(line)