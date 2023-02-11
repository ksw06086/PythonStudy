"""
*** 거북이를 이용해 멋진 글자와 그림을 그릴 수 있도록 기능 구현 ***
1) 마우스 왼쪽 버튼 클릭 : 거북이가 클릭한 지점까지 임의의 색상으로 선을 그리면서 따라옴
2) 마우스 오른쪽 버튼 클릭 : 거북이가 클릭한 지점까지 선을 그리지 않고 이동만 함
3) 마우스 가운데 휠 작동 : 거북이가 임의로 크기를 확대 또는 축소
"""
import turtle
import random
#pSize, tSize = 10, 0;       # 선의 두께, 거북이의 크기
#r, g, b = 0.0, 0.0, 0.0;    # r,g,b 색상 초기화

""" 함수 선언 방법
def 함수명(매개변수) :
    gloval 사용할_전역_젼수
    # 이 부분에 함수 내용을 코딩
"""
"*** 함수 선언 부분 ***"
# 1) 구현 함수
def screenLeftClick(x, y) :
    global r, g, b;
    """turtle.pencolor((r, g, b));
    turtle.pendown();
    turtle.goto(x,y);"""
    
# 2) 구현 함수
def screenRightClick(x,y) :
    turtle.penup();
    turtle.goto(x, y);

# 3) 구현 함수
def screenMidClick(x, y) :
    global r, g, b;
    tSize = random.randrange(1, 10);
    turtle.shapesize(tSize);
    r = random.random();
    g = random.random();
    b = random.random();

"*** 변수 선언 부분 ***"
pSize = 10;
r, g, b = 0.0, 0.0, 0.0;

"*** 메인 코드 부분 ***"
turtle.title('거북이로 그림 그리기');    # 윈도우 창의 제목 지정
turtle.shape('turtle')
turtle.pensize(pSize)   # 그릴 선의 두께 설정

# onscreenclick(함수명, 번호) : 윈도창을 마우스로 클릭하면 '함수명' 함수가 작동됨 / 1은 왼쪽, 2는 가운데, 3은 오른쪽 버튼
turtle.onscreenclick(screenLeftClick, 1)    
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
