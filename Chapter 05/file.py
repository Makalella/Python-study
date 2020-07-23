#
# # file = open("basic.txt", "w")
# #
# # file.write("Hellow Python Programming...!")
# #
# # file. close()
#
# with open("basic.txt", "w") as file:
#     file.write("Hello Python Programming...!")
#
# with open("basic.txt", "r") as file:
#     contents = file.read()
#
# print(contents)
# print()



import random

english = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(english) + random.choice(english)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

with open("info.txt", "r") as file:
    contents = file.read()

print(contents)



with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(",")

        if (not name) or (not weight) or (not height):
            continue
        bmi = int(weight) / ((int(height) / 100 ) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "제체중"

        print("\n".join(["이름 : {}", "몸무게 : {}", "키 : {}", "BMI : {}", "결과 : {}"]).format(name, weight, height, bmi,
                                                                                         result))
        print()


