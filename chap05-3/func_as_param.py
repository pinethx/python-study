# 매개변수 받은 함수 10ㅂ번 호출
def call_10_times(func):
    for i in range(10):
        func()

# 출력 함수
def print_hello():
    print("hello")

#조합
call_10_times(print_hello)