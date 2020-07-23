


try:
    number_input_a = int(input("정수 입력 : "))
    print("원의 반지름 :", number_input_a)
    print("원의 둘레 :", number_input_a * 2 * 3.14)
    print("원의 넓이 :", number_input_a ** 2 * 3.14)
except Exception as except_info:
    # 예외 객체 출력
    print("type(except_info) :", type(except_info))
    print("except_info :", except_info)
print()

##  예외 구분
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("인덱스 정수 입력 : "))
    print("{}번째 요소 : {}".format(number_input_a, list_number[number_input_a]))
except ValueError:
    print("정수를 입력해 주세요")
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")
print()

##  예외 구분 + 예외 객체
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("인덱스 정수 입력 : "))
    print("{}번째 요소 : {}".format(number_input_a, list_number[number_input_a]))
except ValueError as exception:
    print("정수를 입력해 주세요")
    print("exception :", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception :", exception)
print()


## 모든 예외 잡기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("인덱스 정수 입력 : "))
    print("{}번째 요소 : {}".format(number_input_a, list_number[number_input_a]))
    예외.발생()
except ValueError as exception:
    print("정수를 입력해 주세요")
    print("exception :", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception :", exception)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)
print()