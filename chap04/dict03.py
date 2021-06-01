#딕셔너리 선언

dictionary={
    "name" : "7D 건조 망고",
    "type" : "당절임"
}

#요소 제거 전 출력
print("name:", dictionary)

#요소 제거
del dictionary["name"]
del dictionary["type"]

#출력
print("요소 제거 후:", dictionary)