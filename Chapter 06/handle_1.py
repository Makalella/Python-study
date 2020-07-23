
##  숫자 입력
user_input_a = input("정수 입력 : ")

##  입력이 숫자로만 구성되어 있을 때
if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", number_input_a * 2 * 3.14)
    print("원의 넓이 :", number_input_a ** 2 * 3.14)
else:
    print("정수를 입력하지 않았습니다.")
print()


##  try except 구문으로 예외 처리
try:
    number_input_a = int(user_input_a)
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", number_input_a * 2 * 3.14)
    print("원의 넓이 :", number_input_a ** 2 * 3.14)
except:
    print("무언가 잘못되었습니다.")
print()


##  예외되는 부분이 딱히 중요한 부분이 아닐때 except와 pass 조합
try:
    number_input_a = int(user_input_a)
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", number_input_a * 2 * 3.14)
    print("원의 넓이 :", number_input_a ** 2 * 3.14)
except:
    pass
print()


list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass


print("{}내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))
print()


##  try except else 구문
try:
    number_input_a = int(user_input_a)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", number_input_a * 2 * 3.14)
    print("원의 넓이 :", number_input_a ** 2 * 3.14)
print()


##  try except else finally 구문
try:
    number_input_a = int(user_input_a)
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", number_input_a * 2 * 3.14)
    print("원의 넓이 :", number_input_a ** 2 * 3.14)
except:
    print("정수를 입력해 달라고 했잖아요?!")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")
print()


##  fianlly 함수 적용
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

test()
print()

##
print("프로그램이 시작되었습니다.")

while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문의 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("while 함수의 마지막 줄입니다.")
print("프로그램이 종료되었습니다.")
