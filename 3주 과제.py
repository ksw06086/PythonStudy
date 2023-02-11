print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)
print("\n")
print("%f"%123.45)
print("%7.1f"%123.45)
print("%7.3f"%123.45)
print("\n")
print("%s"%"Python")
print("%10s"%"Python")
print("\n")
print("\n줄 바꿈\n연습")
print("\t탭 키\t연습")
print("글자가\"강조\"되는 효과1")
print("글자가\'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")
print("\n")
print('format 사용 -> 10년 : {}년 {}월 {}일'.format(2020+10,9,16))
print("\n")



print("----------별 다이아몬드 출력(2)---------\n")
print("%10s"%"*")
print("%10s"%"***")
print("%10s"%"*****")
print("%10s"%"*******")
print("%10s"%"*********")
print("%10s"%"*******")
print("%10s"%"*****")
print("%10s"%"***")
print("%10s"%"*")

print("\n")
print("\n")
# 진수변환 프로그램
while(1) :
    sel = int(input("입력 진수 결정(16/10/8/2) : "))
    if sel != 16 and sel != 10 and sel != 8 and sel != 2 :
        print("16, 10, 8, 2 숫자 중 하나만 입력하세요.")
        exit()

    num = input("값 입력 : ")
    if sel == 16 :
        num10 = int(num, 16)
    if sel == 10 :
        num10 = int(num, 10)
    if sel == 8 :
        num10 = int(num, 8)    
    if sel == 2 :
        num10 = int(num, 2)

    print("16진수 ==> ", hex(num10))
    print("10진수 ==> ", num10)
    print("8진수 ==> ", oct(num10))
    print("2진수 ==> ", bin(num10))

