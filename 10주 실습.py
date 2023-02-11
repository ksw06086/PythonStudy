"""a = int(input("정수입력 : "))
print("♡"*a)"""

a = input("마지막 숫자를 입력하세요 : ")
for i in range(1, int(a)):
    num = str(i).count('3') + str(i).count('6') + str(i).count('9')
    if num == 0:
        print(i);
    else :
        print("짝"*num)

"""while True:
    a = input("비밀번호를 입력해주세요 : ")
    if len(A) < 8:
        print("비밀번호는 8자리 이상입니다.")
        continue
    if a.isalnum():
        print("비밀번호는 {0}입니다.".format(a))
        break
    else:
        print("비밀번호는 영문자와 숫자로 조합하세요")

"""
#isalpha(), isdigit()
#학적 가년 입력 - 띄어쓰기로 자료 순서대로 입력, 자료 형식이 틀리면 재입력 요구하기
# split, isalpha, isdigit, isalnum, upper, captialize실습
# 이름(대문자), 학번(숫자), 주소(첫글자만 대문자)
"""
while True:
    a = input("Data 입력(이름 학번 주소) :").split()

    if a[0].isalpha() and a[1].isdigit() and a[2].isalnum():
        a[0] = a[0].upper()
        a[2] = a[2].capitalize()
        print(a)
        break
"""
#9 입력한 문자열에서 숫자, 영문 소문자, 영문 대문자, 한글, 기타 문자의 개수를 세는 프로그램을 작성하자.
#힌트) 각 문자는 고유한 번호가 할당 되어 있으며, ord() 함수로 번호를 확인할 수 있다.
#[출력 결과]
#문자열을 입력하세요 : 컴퓨터 소프트웨어공학과 나눔관 5406호에서 Python을 공부하고 있습니다.
#대문자 : 1, 소문자 : 5, 숫자 : 4, 한글 : 26, 기타 : 7
"""
numCnt, lowerCnt, upperCnt, hanCnt, etcCnt = [0]*5
inStr = input("문자열을 입력하세요 : ")

for ch in inStr: #컴퓨터 소프트웨어공학과 나눔관 5406호에서 Python을 공부하고 있습니다.
    if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
        upperCnt += 1
    elif ord(ch) >= ord('a') and ord(ch) <= ord('z'):
        lowerCnt += 1
    elif ord(ch) >= ord('0') and ord(ch) <= ord('9'):
        numCnt += 1
    elif ord(ch) >= ord('ㄱ') and ord(ch) <= ord('힣'):
        hanCnt += 1
    else:
        etcCnt += 1

print("대문자 : ", upperCnt, "소문자 : ", lowerCnt, "숫자 : ", numCnt, "한글 : ", hanCnt, "기타 : ", etcCnt)
"""
"""
def addone(n):
    print(n)
    return n+1

def add(x,y):
    return x+y

num = addone(15)
print(add(10,30))
"""






























