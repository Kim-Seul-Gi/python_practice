#파일 입출력 관련된 것.

# file = open("new.txt","w")#"w"는 쓸 것(write)이다. 이건 덮어쓰는 것이다. 추가가 아니다.
# 추가는 "a"이다.
# file.write("글써졌냐?")
# file.close()

# # 1. 파일 쓰기
# with open("new1.txt","w") as file:
#     ''' 역시도 주석으로 처리한다.
#     with는 컨택스트 매니저라고 부른다.
#     with 블록 내에서 파일을 조작하고, 블록이 끝나게 되면 파일이 닫힌다.
#     '''
#     file.write("글 또 쓰자")

# # 2. 파일 읽기
# with open("new.txt","r") as file: #r은 read
#     line = file.read()
#     print(line)

# # 3. 파일 여러줄 쓰기 new2.txt
# with open("new2.txt","w") as file:
#     for line in range(50):
#         file.write(f"{line}번째 줄입니다.\n") #f를 써야 {}형식을 읽을 수 있다.

# 4. 파일 여러줄 읽기
with open("new2.txt","r") as file:
    # line = file.readline()
    # print(line)
    # line = file.readline()
    # print(line)
    # line = file.readline()
    # print(line)
    # line = file.readline()
    # print(line)

    # while True:
    #     line = file.readline()
    #     if line=='':
    #         breaks
    #     print(line)    
  
    lines = file.readlines() #lines의 type은 list, # type(lines)로 확인 가능
    print(lines)
    print(len(lines))
    print(type(lines))

    for line in lines: #이건  line 전체를 배열로 묶어서 읽는다. list 형식
        print(line) #모든 lines를 다 뽑아버린다 by for문
        
    
    # line = file.readline() #이건 한 줄 한줄만 읽는 string 이다.
    # print(type(line))
    # print(line)
    
    # line = file.readline()
    # print(type(line))
    # print(line)



