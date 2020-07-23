
def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())
print()


def test_1():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

output = test_1()

print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)
print(c)

next(output)