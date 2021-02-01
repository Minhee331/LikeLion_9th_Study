
# print(1+2)
# print("멋쟁이 사자처럼")

# number = 2
# print(number + 1)

# name = input("이름을 입력하세요")

# print(name)

# num1 = input("첫번쨰 숫자를 입력하세요")
# num2 = input("두번쨰 숫자를 입력하세요")
# print(num1 + num2)

# num1 = int(input("첫번쨰 숫자를 입력하세요"))
# num2 = int(input("두번쨰 숫자를 입력하세요"))
# print(num1 + num2)

#숫자형(int)
# num1 = int(input("num1 입력: "))
# num2 = float(input("num2 입력: "))
# print(num1+num2)
#실수형(float)

# 문자열(내장 함수)

#덧셈
# str = "멋쟁이사자처럼"
# str2 = "2주차 스터디 실습 중입니다. "
# print(str*3)
# print(str[0])

#[x:y] --> x번째 인덱스부터 y인덱스 전까지
# print(str[0:4])

#문자열의 길이: len()
# print(len(str))

#문자열 내에서 특정 문자의 등장 횟수: 문자열변수.count('특정문자')
# print(str.count('멋'))

#문자열을 (특정 기준으로) 나누기: 문자열 변수.split()
# print(str2.split()) #공백 기준으로 나눔

#특정 문자 인덱스 찾기: find('문자') , index('문자')
# print(str.find('사'))
# print(str.index('사'))

#리스트 (내장함수)
# li = [3, 1, '지금은', 4, '10시반', 5, 3]
#인덱싱 슬라이싱
# print(li[1])
# print(li[0:2])

#리스트의 길이를 구해주는 함수: len(함수)
# print(len(li))

#리스트 원소 오름차순 정렬해주는 함수: 변수.sort()
# li2 = [3, 1, 4, 5, 3]
# li2.sort()
# print(li2)

#리스트 내의 특정 원소 인덱스 반환해주는 함수: .index()
# print(li.index('10시반'))

#리스트 내의 특정 원소의 갯수 세기:.count(요소)
# print(li.count(3))

#딕셔너리(내장함수)
# pairs = {"잔나비" : '홍콩', '엠맥' : '하루살이', '비투비' :'우리들의 콘서트'}

#하나의 키,벨류 쌍을 추가하는 방법
#변수[key] = value
# pairs['아이유'] = '에잇'
# print(pairs)

#특정 키와 벨류 삭제 방법: del 함수
#del 변수[키]

# del pairs['비투비']
# print(pairs)

#키로 벨류 얻기: 변수.get(키)
# print(pairs.get('잔나비'))

#제어문 - 분기문
#if(조건):
#예제 1
#85점 이상 pass, fail
# score = int(input("점수 입력: "))
# if score >= 85 :
#     print("pass")
# else  :
#     print('fail')


#예제 2
# activity = input("동아리 명: ")
# if activity == "멋쟁이사자처럼":
#     print("나도")
# else:
#     print('아하')

#예제 3
#5000이상 아웃백, 3000이상 학식, 1000이상 컵라면, ㅠㅠ 공기밥
money = int(input("돈: "))

if money>=5000 :
    print("아웃백가자")
elif money >= 3000:
    print("학식 먹자")
elif money >= 1000:
    print("컵라면 먹자")
else:
    print("공기밥 먹자")