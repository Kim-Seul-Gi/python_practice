#input 관련된 기본 코딩

# s = input("인사해주세요!")
# print(s)

# s = input("1+2=")
# print(s)

# s = "인사해주세요"
# print(s)



# 문제 1.
# 문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

# 답 코드

# s = input("문자열을 입력해주세요")
# print("첫 번째 글자는",s[0],"입니다.")
# reverse_s = s[::-1] # 모든 것들을 뒤집어서 보겠다는 뜻
# print("마지막 글자는",reverse_s[0],"입니다.")

# 강사님의 답
# s = input("문자열을 입력해주세요")
# print(s[0])
# print(s[-1])


# 문제 2.
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 답 코드

# n = int(input('숫자를 입력하세요: '))
# a = list(range(1,n+1))
# print("1부터 N까지는")
# for i in a:
#     print(i)
# print("입니다.")

# 강사님의 답

# while 문으로
# n = int(input('숫자를 입력하세요: '))
# i = 0
# while i<n:
#     print(i+1)
#     i += 1

# for 문으로
# n = int(input('숫자를 입력하세요: '))
# for i in range(n):
#     print(1+i)


# 문제 3.
# 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.

# 답 코드

# number = int(input('숫자를 입력하세요: '))
# if number%2==0:
#     print("이 숫자는", "짝수", "입니다.")
# else:
#     print("이 숫자는", "홀수", "입니다.")

#  강사님의 답

# number = int(input('숫자를 입력하세요: '))
# if number % 2:
#     print("홀수") # 0이 아닌 값이 나오면 true이므로 true에 해당하는 홀수가 출력됨.
# else:
#     print("짝수")    

# 문제 4.
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.

'''
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''

# 답 코드

# a = int(input('국어: '))
# b = int(input('영어: '))
# c = int(input('수학: '))
# d = int(input('과학: '))
# if a>=90 and b>80 and c>85 and d>=80:
#     print(True)
# else:
#     print(False)

'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

# prices = input('물품 가격을 입력하세요: ') 

# print(prices)
# print(type(prices))

# prices_list = prices.split(";") # split 으로 문자열 나누기 가능함.
# prices_int = []
# for i in prices_list:
#     prices_int.append(int(i)) # 문자열(str)을 list로 바꾸기 위해서는 for를 사용하자.
# prices_int_sort = sorted(prices_int, reverse=True)
# print(prices_int_sort)


# print(sorted(prices_int, reverse=True)) #prices_int, #print 이 두줄이 이 줄과 같다.

'''
list.sort()
: 원본 자체를 변화시킴. 따라서 list가 정렬되어 있음
: return 되는 값은 none 임

sorted(list)
: 원본을 변화시키지 않음.
: return 되는 것은 정렬된 list임.
'''

 