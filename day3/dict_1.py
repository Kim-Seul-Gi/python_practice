phonebook = {
    # key : value
    "중국집" : "02821",
    "초밥집" : "031",
    "한식집" : "052"
} # 복잡한, 다차원의 딕셔너리를 다룰 것이다.

phonebook2 = dict(중국집=1, 초밥집=2)

# print(phonebook)
# print(phonebook2)

# phonebook["분식집"] = "121312"
# print(phonebook["분식집"]) #key로 접근할 수 있다.

# # 1. 좋아하는 그룹 : key - 이름, value - 나이
# girls_generation = {
#     "tiffany" : 27,
#     "taeyeon" : 28
# } # girls_generation이라는 딕셔너리를 정의한 것이다. 

# 1-2 idol이라는 중첩 dictionary
# idol - key : 그룹명, value : dictionary
# idol = {
#     "girls_generation" : {
#         "tiffany":27,
#         "taeyeon":28
#     },
#     "bts":{
#         "RM" : 24,
#         "지민" : 27
#     }
# }

# for key in phonebook:
#     print(key) #key를 부르는 코드, key 후 자동 엔터 이다.
#     print(phonebook[key]) #value를 부르는 코드

# for key in phonebook:
#     print(key, end='') #key를 부르는 코드, key 띄고 value 후 엔터
#     print(phonebook[key]) #value를 부르는 코드

# for key, value in phonebook.items(): #items를 통해 둘 다 뽑기 가능
#     print(key,value) #key,value 뽑아주는 코드

# for value in phonebook.values(): #value만 뽑아주는 코드
#     print(value)

#zzu.li/dj_dict1