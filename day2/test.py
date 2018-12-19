print('hello world')

#1~100 까지 저장되어 있는 list을 만들고 (a)
#even list 를 만들어서 짝수만 저장 (b)
#odd list 를 만들어서 홀수만 저장 (c)

a = range(1,101) #range(a,b)하면, a 이상 b 미만 생성, list (a) 하면 a 에 있는 것들을 쭉 가져올 수 있다.
# 이 때 a의 class 는 range이다.
# 추가적으로 range(a,b,c)하면, a이상 b 미만 중에서 a a+c a+c+c... b 미만까지 저장한다.
# 모든 리스트에 한해서 나머지가 0이면 even 쪽에 저장, 1 이면 odd 쪽에 저장.
b = []
c = [] # 일단 b,c에 해당하는 폼을 만들어놓자. # 변수 명을 잘 해둡시다..헤헤
# a.append(1) 를 하면 a에 1이 들어가게 된다. 이를 이용해서 해보자.

for i in a: # for 에는 end는 없다. 다만 : 좀 넣자 ~~
    if i%2==0: #원소를 넣는다는 의미니까 i를 쓰는게 맞다~ 추가적으로 문법 익히도록 하자. % 가 나머지에 대한 값
        b.append(i) #if 기준 네 칸을 띄워야 한다. 또는 탭 한번
    else: #else에는 조건이 들어갈 수 없다.
        c.append(i)

print('a는 :',a)
print('b는 :',b)
print('c는 :',c) #print('a','b','c') 하면 abc 다 알려줌





