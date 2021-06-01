import random
print("# random module")

# random() : 0.0 <= x <= 1.0 사이 float 값 리턴
print("- random() : ", random.random())

# uniform(min, max) : 지정한 범위 사이 float 값 리턴
print("- uniform(10, 20) : ", random.uniform(10, 20))

# randrange() : 지정한 범위의 int 리턴
# - randrange(max) : 0부터 max 사이 값 리턴
# - rnadrange(min, max) : min 부터 max 사이 값 리턴
print("- randrange(10) : ", random.randrange(10))

# choice(list) : 리스트 요소 랜덤 선택
print("- choice([1, 2, 3, 4, 5]) : ", random.choice([1, 2, 3, 4, 5]))

# shuffle(list) : 리스트 요소 섞기
print("- shuffle([1, 2, 3, 4, 5]) : ", random.shuffle([1, 2, 3, 4, 5]))

# sample(list, k=<number>) : 리스트 요소 중 k개 출력
print("- sample([1, 2, 3, 4, 5], k=2) : ", random.sample([1, 2, 3, 4, 5], k=2))