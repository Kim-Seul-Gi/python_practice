# # 1. 평균을 구하세요. 여긴 문제
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# # 답변 코드는 아래에 작성해주세요, 1번 문제의 답
# sum = 0
# for key in iu_score:
#     sum = sum + iu_score[key]
# print("1번 문제의 답은",sum/len(iu_score))

# 다른 답
# sum = 0
# for score in iu_score.values(): #딕셔너리의 value값을 바로 가져오는 것
#     sum += score
# average_score = sum / len(iu_score)    
# print(average_score)
# sum(iu_score.values())로도 가능함.

# for key in phonebook: # 여기서부턴 참고자료
#     print(key) #key를 부르는 코드, key 후 자동 엔터 이다.
#     print(phonebook[key]) #value를 부르는 코드

# for key in phonebook:
#     print(key, end='') #key를 부르는 코드, key 띄고 value 후 엔터
#     print(phonebook[key]) #value를 부르는 코드

# for key, value in phonebook.items(): #items를 통해 둘 다 뽑기 가능
#     print(key,value) #key,value 뽑아주는 코드

# for value in phonebook.values(): #value만 뽑아주는 코드
#     print(value)

# for key in iu_score: 
#     print(key) # 이건 iu_score라는 딕셔너리 안에 있는 키 들만 불러오는 것
#     print(iu_score[key]) # 이건 딕셔너리 안에 있는 value만 불러오는 것


# 2. 반 평균을 구하세요.
score = { #스코어의 키는 iu, ui 이고 밸류가 딕셔너리이다.
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}



# 2번 문제의 답. 이건 총평균인듯 - 이해함, 할수있음
# total_score = 0
# length = 0
# for person_score in score.values(): # person_score : {'mat':80, '':90}, {} 꼴로 나옴
#     for individual_score in person_score.values():
#         total_score += individual_score
#         length += 1
# average = total_score/length
# print(average)
    
#이건 혼자 끄적인 것
# sum_iu = 0
# sum_ui = 0
# for key in score:
#     parts = score[key]
#     print(parts)
#         # print(score[key]) #이걸 통해서 각 딕셔너리의 과목:점수 를 가져왔다.
#     for key in parts:
#         sum_iu = sum_iu + parts[key]
#         # print(sum_iu)
#     # for key in part:
#         # print(part[key]) #모든 딕셔너리의 value를 가져왔네...
        
     

#     #sum_iu = sum_iu + score[key]




# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

# 첫 번쨰 값 가져오는 방법

# cold = 0
# hot = 0
# cnt = 0
# hot_city = ""
# cold_city = ""

# for name, temp in city.items():
#     #첫번째 시행때 name="서울", temp = [-6, -10, 5]
#     if cnt == 0:
#         hot = max(temp)
#         cold = min(temp) # 도시별로 최대 최소가 정의된다. 
#         hot_city = name 
#         cold_city = name
#     else:    
#         #최저 온도가 cold보다 추우면, cold에 넣고
#         if min(temp) < cold:
#             cold = min(temp)
#             cold_city = name
#         #최고 온도가 hot보다 높으면, hot에 넣고
#         if max(temp) > hot:
#             hot = max(temp)
#             hot_city = name
#     cnt += 1        
# print(hot_city)
# print(cold_city)
# print(cnt)


# # 이건 전체 평균
# for name, temp in city.items(): #첫번째 시행때 name="서울", temp = [-6, -10, 5]
#     average_temp = sum(temp)/len(temp)
#     print(f"{name}:{average_temp}")

# # 답변 코드는 아래에 작성해주세요.
# print("=====Q3=====")




# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
# print("=====Q4=====")
# if 2 in city["서울"]:
#     print("예")
# else:
#     print("아니오")