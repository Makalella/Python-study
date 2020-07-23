
##  리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)

print("a :", a)
print("b :", b)
print("c :", c)
print("d :", d)
print()

##  괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test :", tuple_test)
print("type(tuple_test) :", type(tuple_test))
print()

a, b, c = 10, 20, 30
print("a :", a)
print("b :", b)
print("c :", c)
print()

##  값 교환
a, b = 10, 20

print("# 교환 전 값")
print("a :", a)
print("b :", b)

a, b = b, a
print("# 교환 후 값")
print("a :", a)
print("b :", b)
print()

##  여러개의 값 리턴
def test():
    return (10, 20)

a, b = test()

print("a :", a)
print("b :", b)
print()
