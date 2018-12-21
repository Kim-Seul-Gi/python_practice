# 181221 practice
import random

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "dj1":  {
            "lecturer": "tak",
            "manager": "pro1",
            "class president": "박성민",
            "groups": {
                "1조": ["강신욱", "윤영우", "이민교", "유창오", "황여진", "김민경"],
                "2조": ["노승만", "이재찬", "이주호", "김예지", "유지원"],
                "3조": ["이민지", "김희윤", "박성민", "조인정", "김슬기", "고병석"],
                "4조": ["임동명", "김승훈", "정상영", "정태현", "한단비", "김동민"]
            }
        },
        "dj2": {
            "lecturer": "junho",
            "manager": "pro2"
        }
    }
}

# 난이도* 1. 지역(location)은 몇개 있나요?

# 답안
location_numbers=ssafy["location"]
print(len(location_numbers))


# 난이도** 2. python standard library에 'requests'가 있나요?

# 답안
py_library=ssafy["language"]["python"]["python standard library"]

# (1) 조건, 반복문으로 할 때의 답안
is_requests = False
for library in py_library:
    if "requests" == library:
        is_requests = True
print(is_requests)

# (2) python 'in' 를 사용할때 답안
print("requests" in py_library)


# 난이도** 3. dj1반의 반장의 이름을 출력하세요.

# 답안
dj1_class_president=ssafy["classes"]["dj1"]["class president"]
print("dj1의 반장은", dj1_class_president, "입니다.")


# 난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.

# 답안
languages=[]
ssafy_language=ssafy["language"]
for key in ssafy_language.keys():
    languages.append(key)
    # print("ssafy에서 배우는 언어들은", key, "입니다.")
print("ssafy에서 배우는 언어들은", languages, "입니다.")

# ssafy["language"].keys()
# ssafy["language"].valuses()
# ssafy["language"].items() : key, value 순으로 출력


# 난이도*** 5 ssafy dj2의 강사와 매니저의 이름을 출력하세요.

# 답안
ssafy_dj2_lecturer=ssafy["classes"]["dj2"]["lecturer"]
ssafy_dj2_manager=ssafy["classes"]["dj2"]["manager"]
print("dj2의 강사는", ssafy_dj2_lecturer, "입니다.")
print("dj2의 매니저는", ssafy_dj2_manager, "입니다.")

# # 다른 답안1

# for key in ssafy["classes"]["dj2"]:
#     print(ssafy["classes"]["dj2"][key])

# # 다른 답안2
# for value in ssafy["classes"]["dj2"].values():
#     print(value) 

# 난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요.

# 답안
ssafy_flask=ssafy["language"]["python"]["frameworks"]["flask"]
ssafy_django=ssafy["language"]["python"]["frameworks"]["django"]
print("flask는", ssafy_flask, "이다.")
print("django는", ssafy_django, "이다.")


# 난이도***** 7. 오늘 당번을 뽑기 위해 groups의 3조 중에 한명을 랜덤으로 뽑아주세요.

# 답안
ssafy_group3=ssafy["classes"]["dj1"]["groups"]["3조"]
worker=random.choice(ssafy_group3)
print("오늘의 당번은",worker)
