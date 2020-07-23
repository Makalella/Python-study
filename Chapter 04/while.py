
##  변수 선언
list_test = [1,2,1,2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)
print()

##  시간과 관련된 기능 가져오기
import time

number = 0
timer = 2
target_tick = time.time() + timer
while time.time() < target_tick:
    number += 1

print("{}초 동안 {}번 반복했습니다.".format(timer, number))
print()

##   break
i = 0

while True:
    print("{}번째 반복문입니다.".format(i))
    i += 1
    input_text = input("종료하시겠습니까?(y) : ")
    if input_text in ["y", "Y"]:
        print("반복문을 종료합니다.")
        break
print()

##  continue
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue
    else:
        print(number)
print()