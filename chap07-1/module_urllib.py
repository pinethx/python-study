# module read
from urllib import request

# urlopen() google main page read
target = request.urlopen("https://google.com")
output = target.read()

# 출력
print(output)