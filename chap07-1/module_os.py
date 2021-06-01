# module read
import os

# 기본 정보 출력
print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부 요소 : ", os.listdir())

# 폴더 생성 및 제거 (비어있을 때만 제거 가능)
os.mkdir("hello")
print(os.path.exists("hello"))
if os.path.exists("hello"):
    os.rmdir("hello")

# 파일 생성 및 이름 변경
with open ("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

if os.path.exists("new.txt"):
    os.remove("new.txt")

std_list = [[1, "std1", 90, 80, 70], [2, "std2", 70, 90, 85]]
if not os.path.exists("std_list.txt"):
    with open("std_list.txt", "m") as file:
        for std in std_list:
            format_str = "{}, {}, {}, {}, {}\n".format(int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4]))
            file.write(format_str)

std_list2 = []

with open("std_list.txt", "r", encoding="utf-8") as file:
    for line in file:
        std = line.strip().split(",")
        print("std : ", std, type(std))
        std= int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4])
        std_list2.append(list(std))

print("파일로 읽어 들인 std_list2[] : ", std_list2)

# cmd 에서 dir 명령어 호출
os.system("dir")