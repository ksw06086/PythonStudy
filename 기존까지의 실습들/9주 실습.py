#9주 실습 김선우 202107045

#1. 복습
secret_msg=""
key_list=[]
value_list=[]
key_list[:] = "abcdefghijklmnopqrstunwxyz"
value_list = list(set('abcdefghijklmnopqrstunwxyz'))
secret_code = dict(zip(key_list, value_list))
#print(secret_code)
for key_, value_ in secret_code.items():
    print('{} -> {}'.format(key_,value_), end=' ') 
msg = list(input("암호화 할 단어를 입력하세요. ==> "))

for i in msg:
    secret_msg+=secret_code[i]
print(secret_msg)

secret_code = dict(zip(value_list, key_list))
for i in secret_msg:
    print(secret_code[i], end = '')

"""secret_msg=""
key_list=[]
value_list=[]
value_list[:] = "abcdefghijklmnopqrstunwxyz"
key_list = list(set('abcdefghijklmnopqrstunwxyz'))
secret_code = dict(zip(key_list, value_list))
#print(secret_code)
for key_, value_ in secret_code.items():
    print('{} -> {}'.format(key_,value_), end=' ') 
msg = list(input("복호화 할 단어를 입력하세요. ==> "))

for i in msg:
    secret_msg+=secret_code[i]

print(secret_msg)
"""

""" msg = input('암호화할 문장을 영어로 입력하세요.')
key = int(input('암호화 키(1~26 숫자)를 입력하세요.'))
encode = ''
for a in msg:
    tmp = ord(a) + key
    print('tmp : ',tmp)
    a = chr(tmp)
    print('a : ',a)
    encode = encode + a
print('평 문:', msg)
print('암호키:', key)
print('암호문:', encode)
"""
