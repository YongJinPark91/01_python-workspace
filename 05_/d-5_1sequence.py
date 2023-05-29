# ###list###
# [표현법] : list [] 안에 ','를 통해 구분을 해준다
# ex) : list_a = [1,2,3,4]
# []내부 가능 문자 : 숫자형, 문자형, 논리형(t/f), 형태를 복합해서도 가능

# 예시 출력
list_a = [1,2,3,4]          # 숫자
list_b = ["a","b","C","d"]  # 문자
list_c = [True, False]      # 논리형
list_d = [1, "a", False]    # 복합형

print(list_a)
print(list_b)
print(list_c)
print(list_d)


# ##list의 인덱싱과 슬라이싱##
numbers = [0,1,2,3,4,5,6,7]

print(numbers[0])
print(numbers[3:5])     # => [3, 4]를 출력, 출력시 슬라이싱이더라도 list형으로 출력됨
print(numbers[1:])      # => [1, 2, 3, 4, 5, 6, 7] 출력
print(numbers[-3:-1])   # => [5, 6] 출력
