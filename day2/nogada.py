import os

# SSAFY_지원자 폴더로 들어가고
os.chdir(r"C:\Users\student\Desktop\python\SSAFY_지원자\SSAFY지원자") # ""안에 있는 것은 절대경로로 수정해도 된다.
# SSAFY 지원자 폴더로 들어가고
#os.chdir(r"SSAFY지원자")
#내용 모두 출력
files = os.listdir()
print(files)
for file in files:
    #os.rename(file, "지원자"+file) #이건 파일 이름에 SAMSUNG을 덧붙이는 방법
    os.rename(file, file.replace("지원자","SSAFY")) #이건 파일 이름에서 지원자를 SSAFY로 바꾸는 법

