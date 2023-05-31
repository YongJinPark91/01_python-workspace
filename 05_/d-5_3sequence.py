# <<<<< tuple >>>>>
# list [] tuple
# tuple 자료형 : numbers = (1,2,3,4,5)
# 수정이 불가한 형태(extend,insert 사용불가)
numbers = 1,2,3,4,5  
numbers1 = 1,  # => 숫자 한개만 하더라도 ' , '을 넣어주어야 함
print(type(numbers))
print(type(numbers1))

# <<<<< Dictionary >>>>>
#[표현법]
#  people(변수명) = {
#     키1 : 값1 ,
#     키2 : 값2 ,
#     키3 : 값3 
# }
#[활용법]
#  print(people["키1"], people["키2]"...)
people = {
    "name" : "김개똥",
    "phone" : "010-1234-5678"
}
print(people["name"],people["phone"])

book = {
    "요가" : ["김요가", "최요가"],  # list 형식으로 넣을수도 있음
    "태권도" : "김태권",
    "1" : "159"
}

books = {
    1 : "one",
    True : "True",     # True는 숫자 1로, False는 숫자 0으로 판별함
    2 : "two"
}

print(books[2])    # []안에 직관적으로 숫자를 넣어 출력을 할 수 있음

# ### 요소를 추가/변경/삭제/확인 하는 방법 ###
coffee = {
    "java" : 2500,
    "ame" : 2500,
    "latte" : 3000
}
# [변경]
# coffee["ame"] = 3000  # 있는 요소에 값을 변경하는 방법

# [추가]
# coffee["hihi"] = 3000  # 없는 요소를 추가하는 방법, 맨뒤로 추가됨

# [삭제]
# del활용 : del coffee["ame"]  # 있는 요소를 삭제
# pop활용 : coffee.pop("java")  # 있는 요소를 삭제

# [확인]
# (.keys())키값 확인 : print(coffee.keys())
# (.values())벨류값 확인 : print(coffee.values())
# (.items())키와 값쌍을 tuple로 확인 : print(coffee.items())

print(coffee)