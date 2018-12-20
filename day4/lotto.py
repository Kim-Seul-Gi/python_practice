import requests
import random
# 1. https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=400
# 위 주소로 요청을 보낸다.


# 2. 응답된 결과를 json으로 바꿔서 dictionary처럼 활용한다. 회차의 당첨번호를 저장했다.

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=400"
response = requests.get(url).json() # response는 json 형식의 dictionary


# 3. 나의 번호를 랜덤으로 로또 번호 하나를 추출한다. 번호 6개 추출함
lotto_numbers = []
for i in range(1,7):
    lotto_numbers.append(response[f"drwtNo{i}"])
bonus = [int(response["bnusNo"])]

# print(lotto_numbers, bonus)

# # 3-1 당첨 번호6개와 랜덤6개가 서로 몇개 겹치는 지 확인

numlist = list(range(1,45))
my_numbers = random.sample(numlist,6)
# print(my_numbers)
# def count_matching_numbers(list1,list2):
#     i=0
#     count=0
#     while i<6:
#         if list1[i] in list2:
#             count = count + 1
#         i = i + 1
#     return count         
# collect_count = count_matching_numbers(my_numbers, lotto_numbers)
# bonus_count = count_matching_numbers(my_numbers, bonus)

# # # 철 번호를 2번으로부터 가져온다.
# if collect_count==6:
#     print("1등")
# elif collect_count==5:
#     if bonus_count==1:
#         print("2등")
#     else:
#         print("3등")
# elif collect_count==4:
#     print("4등")
# elif collect_count==3:
#     print("5등")
# else:
#     print("꽝")        

#여기까지 해서 1회성은 했음       


# for i 
# reallist=lotto_numbers[f"drawNO{i}"]
# 4. 몇 등인지 알아본다. 번호는 1~45
# 1등 : 번호 6개
# 2등 : 번호 5개 + 플러스 번호
# 3등 : 번호 5개
# 4등 : 4개
# 5등 : 3개

'''
파이썬에서는 set 이라는 자료형이 있다.
list를 set으로 형변환을 할 수 있다.
혹은 a = {1,2,5} 직접 만들 수도 있다.
set은 중복된 값을 제거한다.
예) a = [1,2,2]
set(a)
=> [1,2]
set을 통해 합집합(&), 차집합(-), 합집합(|) 을 알 수 있다.
'''





lucky = [0, 0, 0, 0, 0]
for i in range(1000000000000):
    my_numbers = random.sample(range(1, 46), 6)
    matched = len(set(lotto_numbers)&set(my_numbers))

    if matched == 6:
        lucky[0] += 1
        print("당신은",i,"번째에 1등이 되었습니다.")
        print("그 동안의 누적금액은"3100000000*lucky[0]+66000000*lucky[1]*1500000*lucky[2]+50000*lucky[3]+
        5000*lucky[4],"원입니다.")
        break
    elif matched == 5 and bonus in my_numbers:
        lucky[1] += 1
    elif matched == 5:
        lucky[2] += 1
    elif matched == 4:
        lucky[3] += 1
    elif matched == 3:
        lucky[4] += 1 
    print(lucky, i, end='\r')       

