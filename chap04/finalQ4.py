#딕셔너리 선언
character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "찌르기", "밀치기"]
}

#for 문 사용
for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) is list:
        for item in character[key]:
              print(key, ":", item)
    else:
        print(key, ":", character[key])
