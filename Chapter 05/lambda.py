
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)
print()

##  map(), filter()
def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) :", output_a)
print("map(power, list_input_a) :", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a) :", output_b)
print("filter(under_3, list_input_a) :", list(output_b))
print()

##  lambda
power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) :", output_a)
print("map(power, list_input_a) :", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a) :", output_b)
print("filter(under_3, list_input_a) :", list(output_b))
print()

list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) :", output_a)
print("map(power, list_input_a) :", list(output_a))
print()

output_b = filter(lambda x: x < 3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a) :", output_b)
print("filter(under_3, list_input_a) :", list(output_b))
print()