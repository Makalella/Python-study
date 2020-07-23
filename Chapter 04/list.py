
##  리스트 선언
list_a = [1, 2, 3]
list_b = [4, 5, 6]

##  출력
print("# 리스트")
print("list_a =", list_a)
print("list_b =", list_b)
print()

##  기본 연산자
print("# 리스트 기본 연산자")
print("list_a + list_b =", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

##  함수
print("# 길이 구하기")
print("len(list_a) =", len(list_a))

##  리스트 추가 함수
print("# 리스트 뒤에 추가")
list_a.append(5)
print("list_a.append(5) =", list_a)
print("# 리스트 중간에 삽입")
list_a.insert(0, 0)
print("list_a.insert(0, 0) =", list_a)
list_a.insert(4, 4)
print("list_a,insert(4, 4) =", list_a)

##  리스트 제거 함수
print("# 리스트의 특정 요소 제거")
del list_a[0]
print("del list_a[0] =", list_a)
list_a.pop(2)
print("list_a.pop(2) =", list_a)
list_a.pop()
print("list_a.pop() =", list_a)