
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i
    return output

print("1! :", factorial(1))
print("2! :", factorial(2))
print("3! :", factorial(3))
print("4! :", factorial(4))
print("5! :", factorial(5))
print()


def factorial_1(n):
    if n == 0:
        return 1
    else:
        return n * factorial_1(n - 1)

print("1! :", factorial_1(1))
print("2! :", factorial_1(2))
print("3! :", factorial_1(3))
print("4! :", factorial_1(4))
print("5! :", factorial_1(5))
print()

##  재귀함수의 메모화
dictionary = {
    1: 1,
    2: 2
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = output
        return output

print("fibonacci(10) :", fibonacci(10))
print("fibonacci(20) :", fibonacci(20))
print("fibonacci(30) :", fibonacci(30))
print("fibonacci(40) :", fibonacci(40))
print("fibonacci(50) :", fibonacci(50))
print()
