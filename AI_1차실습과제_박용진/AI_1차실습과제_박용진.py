# random이라는 메소드는 임의의 숫자, 난수를 생성하기 위한 구문
import random

# 윷놀이의 가능한 결과가 나타나는 문자열
yut = ['xxxx','xxxo','xxox','xxoo','xoxx','xoxo','xoox','xooo','oxxx',
       'oxxo','oxox','oxoo','ooxx','ooxo','ooox','oooo']

# yut리스트에서 무작위로 하나를 뽑아서 throw에 저장하는 역할
throw = random.choice(yut)

# 결과 출력
print(throw)

# 'o'의 갯수를 세서, 'n'에 저장
n = throw.count('o')

# 4일경우 모
if n == 4:
    print("모")
# 3일 경우 도
elif n == 3:
    print("도")
# 2일 경우 개
elif n == 2:
    print("개")
# 3일 경우 걸
elif n == 1:
    print("걸")
# 3일 경우 윷
elif n == 0:
    print("윷")