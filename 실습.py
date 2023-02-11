id = input('ID : ')
pwd = input('password : ')

if len(id)<10:
    if len(pwd) <10:
        print("회원가입 성공")
    else :
        print("회원가입 실패! password 길이가 10을 초과")
else :
    print("회원가입 실패! ID 길이가 10을 초과")


id = 'abv'
pw = '456'

input_id = input('ID : ')
input_pwd = input('password : ')

if id != input_id:
    print("로그인 실패 : id오류")
else :
    if pw != input_pw:
        print("로그인 실패 : password 오류")
    else :
        print("로그인 성공")

eng = int(input("영어 점수 입력 "))
math = int(input("수학 점수 입력 "))
total = eng+math

if total < 110:
    print("불합격 : 종합점수가 부족합니다.")

elif eng>=40:
    if math>=40:
        print("합격")
    else :
        print("불합격 : 수학 점수가 부족합니다.")
else :
    print("불합격 : 영어 점수가 부족합니다.")

num = int(input("합계를 계산한 숫자를 입력하세요"))
hap = 0

for i in range(1,num+1):
    hap += i

print("1부터 %d 까지의 합계는 %d 입니다"%(num,hap))

import random
number=[]
for num in range(0, 10):
    number.append(random.randrange(0,10))

print("생성된 리스트 : ", number)

for num in range(0,10):
    if num not in number:
        print("숫자 %d는(은) 리스트에 없습니다."%num)



