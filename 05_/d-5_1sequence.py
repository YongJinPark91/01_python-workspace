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


# ###list안에 문자열이 있는경우###
list_lang = ["JAVA", "C", "Python", "GO"]

print(list_lang[0])      # => JAVA가 출력됨 // [n]를 한개만 준다면 문자열의 ','를 기준으로 순서를 파악하여 출력해줌
print(list_lang[0][0])   # => J가 출력됨    // [n]는 ','를 기준으로 n번째 문자열을 출력해주고, 두번째[m]는 그 문자열의 m번째 인덱스를 출력해줌
print(list_lang[2][2:4]) # => th가 출력됨   // [n]에서 선언된 문자열에서 [n:m] n~부터 m-1번째 까지의 문자를 출력해줌 


# ###요소를 수정###
list_lang[1] = "C++"     # => C가 C++로 변경됨
print(list_lang)         # C++로 변경된 상태로 출력됨


# ###슬라이스를 활용한 수정###
list_lang[1:3] = ["C#", "Python3"]     # => C++을 C#으로, Python을 Pyhon3로 변경
# 위 예시는 2개만을 선정하고, 2개를 수정한 형태
# 2개를 선정하고, 3개를 수정하면 인덱스 1~2을 수정하고, 1개를 추가함
# 2개를 선정하고, 1개를 수정하면 인덱스 1번만 변경하고 2번을 제외함
print(list_lang)


# ###len 함수를 활용한 출력###
# 기본형태 : len(변수)          => 변수내의 요소의 개수를 출력해줌
print(len(list_lang))


# ### append()를 활용한 요소의 추가###
# append() 리스트 맨 뒤에 추가하는 함수
list_lang.append("Ruby")
print(list_lang)
# 사용시 주의사항 요소를 추가하면 원하는 결과가 나오지 않음
list_a = [1,2,3]
list_lang.append(list_a)
print(list_lang)         # 출력결과 : ['JAVA', 'C#', 'Python3', 'GO', 'Ruby', [1, 2, 3]]
                         # 출력결과를 ['JAVA', 'C#', 'Python3', 'GO', 'Ruby', 1, 2, 3] 처럼 얻고 싶지만 []까지 추가된 것을 볼 수있다.


# ### extend()를 활용한 요소의 추가 ###
list_lang1 = ["JAVA", "C", "Python", "GO"]
list_b = [1,2,3]
list_lang1.extend(list_b)
print(list_lang1)        # 출력결과 : ['JAVA', 'C', 'Python', 'GO', 1, 2, 3]
                         # list_lang1의 []내에 값이 들어간 것을 볼 수 있다.
list_lang1.extend("JAVA")
print(list_lang1)        # 출력결과 : ['JAVA', 'C', 'Python', 'GO', 1, 2, 3, 'J', 'A', 'V', 'A']
                         # JAVA가 한개의 문자씩 추가된 것을 볼 수 있다.


# ### insert(index, data) ###
# 원하는 위치에 인덱스를 추가할 수 있는 함수
list_lang1.insert(0,"R")
print(list_lang1)        # 출력결과 : ['R', 'JAVA', 'C', 'Python', 'GO', 1, 2, 3, 'J', 'A', 'V', 'A']
                         # 0번 인덱스에 'R'이 추가된 것을 볼 수 있다.


# <<<<< 요소를 삭제하는 방법 >>>>>
# ### pop() ###
# 마지막 요소를 반환을 해주고 삭제가 됨
# 표현법 : 변수.pop(n)

# ### remove() ###
# 해당 요소를 직접적으로 지정하여 삭제하는 방법
# 안에 어떤 문자열이 있는지 알고 있다면 사용가능 방법
# 표현법 : 변수.remove("삭제할 문자(열)")

# ### del ###
# 표현법 : del 변수[n]
# 해당인덱스 위치의 요소가 삭제가 됨


# <<<<< 리스트의 정렬 >>>>>
numbers1 = [1,100,3,17,250,6,77,1530]

# ### sort() ###
# 오름차순 정렬(작은수 >>> 큰수)
numbers1.sort()
print(numbers1)
# 내림차순 정렬(큰수 >>> 작은수)
numbers1.sort(reverse = True)    # True처럼 t를 꼭 대문자로 작성해야함
print(numbers1)
# 오름차순, 내림차순은 숫자뿐만아니라 문자도 가능하다


# ### reverse() ###
# 요소를 역순으로 변경해주는 함수
numbers2 = [5,1,100,3,17,250,6,77,1530]
numbers2.reverse()
print(numbers2)



# <<<리스트 내부에서 특정값이 포함되어 있는지 확인>>>
# in 연산자와 not in 연산자

# ### in ###
# 사용방법 : 확인할 문자/숫자 in 변수명  => prtin(50(확인할 숫자) in numbers(변수명))
                                     # => prtin("JAVA"(확인할 문자) in numbers(변수명))
# 출력 : 포함되어 있다면 True, 없다면 False로 출력됨                                     

# ### not in ###
# 사용방법 : 확인할 문자/숫자 not in 변수명  => prtin(50(확인할 숫자) not in numbers(변수명))
                                     # => prtin("JAVA"(확인할 문자) not in numbers(변수명))
# 출력 : 포함되어 있지 않다면 True, 있다면 False로 출력됨                                     



