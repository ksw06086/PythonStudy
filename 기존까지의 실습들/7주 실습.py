for i in range(0,5):
    print(' '*i, '*' * (9-(i-2)))

import random
com_num = random.randrange(1,51)
my_num=0
for i in range(1,6):
    my_num = int(input("예상하는 {}번째 숫자를 입력하세요. : ".format(i)))
    if com_num == my_num:
        print("정답입니다")
        break
    elif com_num > my_num :
        print('UP')
    else :
        print('DOWN')
print("끝")


"""
import random

num_list = []
n=0
while len(num_list) < 7:
    n=random.randint(1,46)
    if n not in num_list:
        num_list.append(n)

print('내 번호'.center(22,'-'))
print(sorted(num_list))
"""
"""
import random

winnumber=5,12,23,36,39,42
num_list=[]
n=0
while len(num_list) < 7:
    n=random.randint(1,46)
    if n not in num_list:
        num_list.append(n)

print('내 번호'.center(22,'-'))
print(sorted(num_list))
print()

for i in range(6) : 
    if num_list[i] in winnumber:
        print('(',num_list[i], ': O)',end=', ')
    else :
        print('(',num_list[i], ': X)',end=', ')
"""

"""
yours = random.randint(1,3)
if yours == 1:
    yours = '가위'
elif yours == 2:
    yours = '바위'
else :
    yours = '보' """
"""
win_dic={'가위':'보','바위':'가위','보':'바위'}
msg = {1:'나',2:'너',3:'비김'}

rep = ['가위','바위','보']
yours = random.choice(rep)

winner = 0
mine = input('가위 바위 보 중 하나만 입력 : ')

while(mine != '가위' and mine != '바위' and mine != '보')  :
    mine = input('가위 바위 보 중 하나만 입력해주세요 : ')


if mine == yours :
    winner = 3
elif win_dic[mine] == yours:
    winner = 1
else :
    winner = 2
"""
"""
if (mine == '가위' and yours == '바위') or (mine == '바위' and yours == '보') or (mine == '보' and yours == '가위') :
    winner = '너'
elif (mine == '가위' and yours == '보') or (mine == '바위' and yours == '가위') or (mine == '보' and yours == '바위') :
    winner = '나'
else :
    winner = '비김'
"""

print('----------------------------------')
print('        나         너                   승자')
print('----------------------------------')
print('      {:^3}      {:^3}              {:^3}'.format(mine,yours,msg[winner]))

""" 8주차 영상 -> 시험본 후에 해도 됨, 밴드에 공지 할 것 """
""" 튜플 """
