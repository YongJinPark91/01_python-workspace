# ###정말 많이 쓰는 자료구조###
# index는 문자를 하나씩 밖에 추출할수 없지만
# 슬라이싱은 문자를 잘라서 추출하는 방법이다.

# 문법 print("추출을 원하는 숫자/문자열"(양수)[n:m]/(음수)[m:n]))
#  n : 처음으로 출력될 순번
#  m : 마지막으로 출력될 순번
#   * 마지막 위치인 m의 위치는 출력되지 않음. (n~m-1번째까지 출력됨)
#  Tip. step 활용 : print("문자/숫자열"[n:m:s])  => s는 s배 번째의 자료를 출력함
#                                               => s가 음수일 경우 뒤에서 s배 번째의 자료를 출력
#           * 예) : print("012345"[0:4:2]  => 0번부터 4번까지 중에 2배수 번째 들어있는 문자를 출력 => 1, 3 출력
                  

# <예제1>
str_slice = "0123456789"

print(str_slice[0:7])  # => 0123456 이 출력됨
print(str_slice[2:])   # => 2~끝까지  (m의 위치가 공백이면 n번부터 끝까지 출력됨)
print(str_slice[:7])   # => 처음부터~7번까지  (n의 위치가 공백이면 처음부터 m번까지 출력됨)
print(str_slice[:])    # => 전체가 출력됨

print("===========구분선===========")

# <예제2>
str_slice1 = "Python is easy"

# 음수를 사용해 출력
print(str_slice1[:-1])      # y를 뺀 전체 출력
print(str_slice1[-14:])     # 전체가 출력됨
print(str_slice1[-1:-14])   # 문자열이 나오지 않음
print(str_slice1[0:18])     # 문자슬라이싱은 인덱싱과 다르게 범위 외의 부분을 넣더라도 정상적으로 출력됨

print("===========구분선===========")

# <예제3>
str_slice2 = "0123456789"
print(str_slice2[::2])       # 앞에서부터 2배수 자리 출력 (02468)
print(str_slice2[::-2])      # 뒤에서부터 2배수 자리 출력 (97531)

print("===========구분선===========")

# <예제4>
# 슬라이스와 연산자를 혼합한 출력

str_slice3 = "Python"

print(str_slice3[0:] + str_slice3[::-1]) # PythonnohtyP 출력
#  결과값 :  Python  + 결과값 :  nohtyP 

print(str_slice3[1:5] + str_slice3[0] + str_slice3[5]) # ythoPn 출력
#  결과값 :  ython    +      P        +      n