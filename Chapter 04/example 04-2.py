
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1},
]

for dictionary in pets:
    print("{} {}살".format(dictionary["name"], str(dictionary["age"])))
print()

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(counter)
print()

print(type([]) is list)
print()

##  딕셔너리 선언
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skiil": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for element in character[key]:
            print(key, ":", element)
    else:
        print(key, ":", character[key])