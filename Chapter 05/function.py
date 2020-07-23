

def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print("def print_3_times()")
print_3_times()
print()

def print_n_times(value, n):
    for i in range(n):
        print(value)

print("def print_n_times(value, n), value = \"Hi\", n = 4")
print_n_times("Hi", 4)
print()

def print_v_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print("가변 변수 print_v_times(n, *values)")
print_v_times(3, "안녕하세요", "즐거운", "파이썬")
print()

def print_x_times(value, n=2):
    for i in range(n):
        print(value)

print("매개변수 = x의 함수 print_x_times(value, n=2)")
print_x_times("안녕하세요")
print()

def test(a, b=10, c=100):
    print(a + b + c * 2)

print("def test(a, b=10, c=100)")
print("a + b + 2c")
print("test(10, 20, 30)")
test(10, 20, 30)
print("test(a=10, b=100, c=200)")
test(a=10, b=100, c=200)
print("test(c=200, a=10, b=100)")
test(c=200, a=10, b=100)
print("test(10, c=200)")
test(10, c=200)
print()

def return_test():
    print("A")
    return
    print("B")

return_test()


def return_test1():
    return 100

value1 = return_test1()
print(value1)

def return_test2():
    return

value2 = return_test2()
print(value2)
print()


def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print("Sum from 0 to 100 :", sum_all(0, 100))
print("Sum from 0 to 1000 :", sum_all(0, 1000))
print("Sum from 50 to 100 :", sum_all(50, 100))
print("Sum from 50 to 1000 :", sum_all(50, 1000))
print()


def sum_all(start = 0, end = 100, step = 1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end = 100))
print("C.", sum_all(end = 100, step = 2))
print()