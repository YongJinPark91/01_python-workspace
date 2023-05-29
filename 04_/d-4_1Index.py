# 인덱스라는 문자열을 만들고 글자를 하나씩 빼내어 본다.

#문법 : print("추출을 원하는 문자/숫자 열" [n])
#       n번째의 문자/숫자 추출(0부터 시작)

# index라는 문자열에서 글자를 뽑을때
#  i  n  d  e  x 
#  0  1  2  3  4 
# -5 -4 -3 -2 -1 의 순서대로 글자가 출력된다
# 음수의 경우에는 맨뒤가 -1부터 시작된다.

# 양수로 글자를 추출하는 경우#
print("index"[0])
print("index"[1])
print("index"[2])
print("index"[3])
print("index"[4])

print("===========구분선===========")

# 음수로 글자를 추출하는 경우#
# 음수 끝의 시작은 0부터 시작하지 않는다.
# 음수는 제일 뒤부터 추출이 된다
print("index"[-5])
print("index"[-4])
print("index"[-3])
print("index"[-2])
print("index"[-1])

print("===========구분선===========")
# String index 라는 문자열을 출력
str_ = "String index"   # str_에 "String index"라는 문자열을 대입

print(str_[0])
print(str_[1])
print(str_[2])
print(str_[3])
print(str_[4])
print(str_[5])
print(str_[6])
print(str_[7])
print(str_[8])
print(str_[9])
print(str_[10])
print(str_[11])
# print(str_[12]) // 13번째 글자가 없기 떄문에 오류발생(IndexError: string index out of range // 범위를 벗어남)
# 문자열을 인덱스 할 경우 문자열 내에 출력을 하는게 중요하다.

print("===========구분선===========")