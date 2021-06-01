#딕셔너리 선언
pets = [
    {"name":"구름", "age":5},
    {"name":"초코", "age":3},
    {"name":"아지", "age":1},
    {"name":"호랑이", "age":1}
]

#타이틀 출력
print("# 우리 동네 애완 동물들")

#for 반복문
for key in pets:
    #출력내용
    print(key["name"], str(key["age"])+"살")