
##  대소문자 바꾸기 upper(), lower()
a = "Hello Python Programming...!"

print("# 대소문자 바꾸기")
print("원본 a : ", a)
print("a.upper() : ", a.upper())
print("a.lower() : ", a.lower())
print()

##  문자열의 공백 제거
##  strip() : 양옆 공백 제거
##  lstrip() : 왼쪽의 공백 제거
##  rstrip() : 오른쪽의 공백 제거
input_a = """
        안녕하세요
    문자열의 함수를 알아봅니다.
"""

print("원본 : \n", input_a)
print("strip() :\n", input_a.strip())
print()

##  문자열의 구성 파악 : isOO()

##  문자열 찾기
##  왼쪽부터 찾아서 첫 등장하는 위치 : find()
##  오른쪽에서부터 찾아서 첫 등장하는 위치 : rfind()
output_a = "안녕안녕하세요".find("안녕")
output_b = "안녕안녕하세요".rfind("안녕")

print(output_a)
print(output_b)
print()

##  해당 문자열이 있는지 확인 : in
print("안녕" in "안녕하세요")
print("잘자" in "안녕하세요")
print()

##  문자열 자르기 : split()
a = "10 20 30 40 50".split(" ")
print(a)