# "from test package import *"으로 모듈 읽어 들일 때 가져올 모듈
__all__ = ["module_a", "module_b"]

# 패키지를 읽어 들일 때의 처리
print("test_package 를 읽어 들였습니다.")