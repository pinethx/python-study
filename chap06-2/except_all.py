# 변수 선언
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외처리
try:
    # 숫자 input
    number_input = int(input("정수 입력 >"))
    # 리스트 요소 출력
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as execption:
    # ValueError 발생
    print("정수를 입력하세요.")
    print(type(execption), execption)
except IndexError as execption:
    # IndexError 발생
    print("리스트의 인덱스를 벗어났습니다.")
    print(type(execption), execption)
except Exception as execption:
    # 이외의 예외 발생
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(execption), execption)