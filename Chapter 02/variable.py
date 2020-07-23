
##  변수 선언과 할당
pi = 3.14159265
r = 10

##  변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*pi*r)
print("원의 넓이 =", pi*r*r)
print()

## 숫자 복합 대입 연산자 (+=, -=, *=, /=, %=, **=)
## 문자열 복합 대입 연산자 (+=, *=)
number = 100
number += 20
print(number)
number /= 10
print(number)
number %= 5
print(number)
number **= 4
print(number)
print()

string = "안녕하세요"
string += "!"
print(string)
string *= 2
print(string)
print()

##  사용자 입력을 받는것은 input() 함수
##  입력은 숫자로해도 무조건 문자열로 받음
string = input("인사말을 입력하세요 : ")
print(string)
print(type(string))
print()

number = input("숫자를 입력하세요 : ")
print(number)
print(type(number))
print()

##  문자열을 숫자로 바꾸는 함수는 int(), float() 이다.
##  단 입력한 문자열 자체가 실수이면 int()로 변환시 에러가 발생한다.
string_a = string
int_a = int(string_a)
string_b = number
int_b = int(string_b)

print("문자열 자료 :", string_a + string_b)
print("숫자 자료 :", int_a + int_b)

##  숫자를 문자열로 바꾸는 함수는 str()이다.

