
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
str = "멋쟁이사자처럼"
str2 = "2주차 스터디 실습 중입니다. "
print(str*3)
print(str[0])

#[x:y] --> x번째 인덱스부터 y인덱스 전까지
print(str[0:4])

#문자열의 길이: len()
print(len(str))

#문자열 내에서 특정 문자의 등장 횟수: 문자열변수.count('특정문자')
print(str.count('멋'))

#문자열을 (특정 기준으로) 나누기: 문자열 변수.split()
print(str2.split()) #공백 기준으로 나눔

#특정 문자 인덱스 찾기: find('문자') , index('문자')
print(str.find('사'))
print(str.index('사'))
