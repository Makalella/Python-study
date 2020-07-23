
import os

print("현재 운영체제 :", os.name)
print("현재 폴더 :", os.getcwd())
print("현재 폴더 내부의 요소 :", os.listdir())

# 폴더를 만들고 제거 (제거의 경우 폴더가 비어 있어야 가능)
os.mkdir("Hello")
os.rmdir("Hello")

# 파일을 생성하고 파일이름 변경
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일을 제거합니다.
os.remove("new.txt")
# os.unlink("new.txt"

os.system("dir")