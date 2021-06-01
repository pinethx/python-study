def print_n_times(*values, n=2):
    # n번 반복
    for i in range(n):
        # values는 리스트처럼 활용
        for value in values:
            print(value)
        # 줄바꿈
        print()

# 함수호출
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)