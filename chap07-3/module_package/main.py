# module read
# import test_package.module_a as a
# import test_package.module_b as b

# 패키지 내부 모듈 모두 호출
from test_package import *

# 모듈 내부 변수 출력
print(module_a.variable_a)
print(module_b.variable_b)