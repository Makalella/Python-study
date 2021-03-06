
##  \" or \'는 문자열과 상관없이 사용할 수 있는 따옴표

print('"안녕하세요"라고 말했습니다.')
print("\"안녕하세요\"라고 말했습니다")
print()

print("'안녕하세요'라고 말했습니다.")
print('\'안녕하세요\'라고 말했습니다.')
print()

##  \n은 줄바꿈, \t는 tab
print("안녕하세요\n안녕하세요")
print()
print("안녕하세요\t안녕하세요")
print()

print("이름\t나이\t지역")
print("윤인성\t25\t\t강서구")
print("윤아린\t24\t\t강서구")
print("구름\t3\t강서구")
print()

## \\는 역 슬래시
print("\\ \\ \\ \\")
print()

##  """ 따옴표 3개는 enter시 자동 줄바꿈 ('''도 가능)
print("동해몰과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세\n무궁화 삼천리 화려강산\n대한사람 대한으로 길이 보전하세")
print()
print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세""")
print()

##  \를 줄바꾸는 곳에 삽입시 코드를 볼떄 편하게 하기 위해서 사용하는 enter를 무시
print("""동해물과 백두산이 마르고 닳도록\
하느님이 보우하사 우리나라 만세\
무궁화 삼천리 화려강산\
대한사람 대한으로 길이 보전하세""")

##  문자열 연결 연산자중 +의 경우 문자열끼리의 연결은 가능하지만, 문자열+숫자는 불가능

##  문자 선택 연산자(인덱싱)[]
print("문자 선택 연산자에 대해 알아볼까요?")
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
print()
print("문자를 뒤에서부터 선택해 볼까요?")
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])
print()

## 문자열 범위 선택 연산자(슬라이싱)[:]
print("안녕하세요"[1:4])
print("안녕하세요"[1:])
print("안녕하세요"[:3])
print()

hello = "안녕하세요"
print(hello[1:4])
print(hello[1:])
print(hello[:3])
print()

## 문자열의 길이 len()함수
print(len("안녕하세요"))
print(len(hello))
