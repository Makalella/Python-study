
##  비교 연산자 : ==, !=, <, >, <=, >=
##  알파벳이나 한글 비교의 경우 'a'와 'ㄱ'이 빠른 번호이다.

##  논리 연산자 : not, and, or
##  not의 경우 반대 출력
##  and, or의 경우 진리표와 같음
x = 10
under_20 = x < 20
print("under_20 :", under_20)
print("not under_20 :", not under_20)
print()

if True:
    print("True 입니다.")
    print()

if False:
    print("False 입니다.")
    print()

if 1:
    print("True 입니다.")
    print()

if 0:
    print("False 입니다.")
    print()

##  부호 판단
number = input("정수 입력 : ")
number = int(number)

if number > 0:
    print("양수 입니다.")

if number < 0:
    print("음수 입니다.")

if number == 0:
    print("0 입니다.")