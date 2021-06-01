#숫자 입력
numbers = [1,2,6,8,4,3,2,1,4,5,6,7,8,9,9,0,0,7,6,4,5,6,7]
counter={}

#for 반복문
for number in numbers:
    #내용
    if number in counter:
        counter[number] = counter[number]+1
    else:
        counter[number] =1

#출력
print(counter)