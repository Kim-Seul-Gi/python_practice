import requests
import random
# 완성되지 않은 파일이다.
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=400"
response = requests.get(url).json() # response는 json 형식의 dictionary

#로또 넘버를 불러오기
lotto_numbers = []
for i in range(1,7):
    lotto_numbers.append(response[f"drwtNo{i}"])
bonus = [int(response["bnusNo"])]

print(lotto_numbers, bonus)

#내가 뽑은 번호
numlist = list(range(1,45))
my_numbers = random.sample(numlist,6)
print(my_numbers)



def counting(numlist, lotto_numbers):
    numlist = list(range(1,45))
    my_numbers = random.sample(numlist,6)
    def count_matching_numbers(list1,list2):
        i = 0
        count=0
        while i<6:
            if list1[i] in list2:
                count = count + 1
                i = i + 1
                return count  
            collect_count = count_matching_numbers(my_numbers, lotto_numbers)
            bonus_count = count_matching_numbers(my_numbers, bonus)
    m=0
    countm=0
    while m<100000000000:
        if collect_count==6:
            print(countm)
            break
        else:
            countm = countm + 1
            m=m+1


