#딕셔너리 선언
dictionary={
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

#사용자로부터 입력 받기

key = input("> 접근하고자 하는 키 : ")

#출력
if key in dictionary:
    print(dictionary[key])
else:
    print("해당 키는 존재하지 않습니다.")