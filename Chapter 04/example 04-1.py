
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print("- 100 이상의 수 :", number)
print()

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    odd_even = number % 2
    if odd_even == 1:
        print("{}는 홀수 입니다.".format(number))
    else:
        print("{}는 짝수 입니다.".format(number))
print()

for number in numbers:
    print("{}는 {} 자릿수 입니다.".format((number), len(str(number))))
print()

list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]

for list in list_of_list:
    for element in list:
        print(element)
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number + 2) % 3].append(number)

print(output)