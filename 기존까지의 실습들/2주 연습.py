## a=100
## b=50
## a,b = 100,50
"""a = int(input("첫번째 숫자를 입력하세요 : "))
b = int(input("두번째 숫자를 입력하세요 : "))
result=a+b
print(a, "+", b, "=", result)
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)
print(a, "/", b, "=", a/b) """
## 계산기
""" op1 = int(input("계산할 첫번째 숫자를 입력하세요 : "))
oper = input("연산자를 입력하세요 : ")
op2 = int(input("계산할 두번째 숫자를 입력하세요 : "))
result=0

if oper == "+" :
    result = op1+op2
if oper == "-" :
    result = op1-op2
if oper == "*" :
    result = op1*op2
if oper == "/" :
    result = op1/op2

print(op1, oper, op2, "=", rsult) """

## 1. x,y에 각 11, 22를 할당하고, 그 후 숫자를 직접 이용하지 않고 다른 변수 z를 이용하여 두수를 교환하는 프로그램
"""x = 11
y = 22
print("x = ", x, ", y = ", y)
z = x
x = y
y = z
print("x = ", x, ", y = ", y, ", z = ", z)"""

## 3. 사용자가 x의 값을 입력하게 하여 자신의 이름 앞과 뒤에 입력한 x만큼 '*'를 표시하는 프로그램을 작성하시오.
x=int(input(">>> "))
print('*'*x, "송혜교", '*'*x)

