
str_input = input("숫자 입력 : ")
num_input = float(str_input)

print()
print(num_input, "inch")
print(num_input * 2.54, "cm")
print()

a = input("문자열 입력 : ")
b = input("문자열 입력 : ")

print()
print(a, b)
c = a
a = b
b = c
print(a, b)