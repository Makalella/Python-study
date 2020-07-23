
##  짝 / 홀 판단 1
number = input("정수 입력 : ")
last_character = number[-1]
last_number = int(last_character)

if last_number == 0 \
    or last_number == 2 \
        or last_number == 4 \
        or last_number == 6 \
        or last_number == 8:
    print("짝수 입니다.")

if last_number == 1 \
    or last_number == 3 \
        or last_number == 5 \
        or last_number == 7 \
        or last_number == 9:
    print("홀수 입니다.")

##  짝 / 홀 판단 2
if last_character in "02468":
    print("짝수 입니다.")

if last_character in "13579":
    print("홀수 입니다.")

##  짝 / 홀 판단 3
number = int(number)

if number % 2 == 0:
    print("짝수 입니다.")

if number % 2 == 1:
    print("홀수 입니다.")

##  else 사용
if number % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수 입니다.")
print()

##  elif 사용
import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print("봄입니다.")
elif 6 <= month <= 8:
    print("여름입니다.")
elif 9 <= month <= 11:
    print("가을입니다.")
else:
    print("겨울입니다.")
print()

##  앞에서 검사했던 조건은 제외하여 코드 최적화
score = float(input("학점을 입력하세요(0 ~ 4.5) : "))

if score == 4.5:
    print("신")
elif 4.2 <= score:  # 4.2 <= score < 4.5와 같음
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 < score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")
