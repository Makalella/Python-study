
dict_a = {
    "name" : "어밴저스 엔드게임",
    "type" : "히어로 무비"
}

print(dict_a)
print()

##  딕셔너리 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트룸", "치자황색소"],
    "origin": "필리핀"
}

##  출력
print("name :", dictionary["name"])
print("type :", dictionary["type"])
print("ingredient :", dictionary["ingredient"])
print("origin :", dictionary["origin"])
print()

##  값 변경
dictionary["name"] = "8D 건조 망고"
print("name :", dictionary["name"])
print()

##  딕셔너리 선언
dictionary = {}
print(dictionary)

##  딕셔너리에 요소 추가
dictionary["name"] = "새로운 이름"
dictionary["head"] = "새로운 정신"
dictionary["body"] = "새로운 몸"

##  출력
print("요소 추가 이후 :", dictionary)
print()

##  딕셔너리 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트룸", "치자황색소"],
    "origin": "필리핀"
}

for key in dictionary:
    print(key, ":", dictionary[key])