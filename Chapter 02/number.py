
##  type 확인 함수 type()
print(type(52))
print(type(35.125))

##  10의 지수승 표현은 e or E로 함
print(3.14e2)
print(3.14E2)
print(3.14e-2)
print(3.14E-2)
print()

##  사칙연산은 모두 가능 (연산 우선순위도 같음)
##  정수 나누기 연산자 // : 정수부분만 출력
##  나머지 연산자 % : 몫을 제외한 나머지를 출력
##  제곱 연산자 ** : 앞의 숫자를 뒤의 숫자만큼 제곱함
print("5 / 2 =", 5/2)
print("5 // 2 =", 5//2)
print("5 % 2 =", 5%2)
print("2 ** 3 =", 2**3)
print("5 ** 2 =", 5**2)
print()

##  연습문제
print("# 기본적인 연산")
print(15, "+", 4, "=", 15+4)
print(15, "-", 4, "=", 15-4)
print(15, "*", 4, "=", 15*4)
print(15, "/", 4, "=", 15/4)
print()
print("#3464를 17로 나누었을 때의")
print("- 몫 :", 3462//17)
print("- 나머지 :", 3462%17)
print()
print(2+2-2*2/2*2)
print(2-2+2/2*2+2)