# ## 산술 연산자 ###
# 산술연산자의 종류
# 1. 기본연산자 = + , - , * , /
# 2. 몫을 구하는 연산자 = //
# 3. 나머지를 구하는 연산자 = %
# 4. 제곱을 구하는 연산자 = **

# print(10 + 2)
# print(10 - 2)
# print(10 * 2)
# print(10 / 2)  # 결과 : 5.0 // 정수형의 나숫셈결과는 무조건 실수형으로 나온다

# print(type(10/10))  # 몫이 1이여도 1.0d으로 결과를 반환해 주고
#                     # 데이터 타입도 float형으로 반환된다.

# print(10 // 2)      # //은 몫만을 구하는 연산자로서 정수단위로 결과를 준다.
# print(type(10 // 2))# 데이터 타입도 int형으로 반환된다.

# print(10 % 3)       # 10을 3으로 나눈 나머지는 1이다.



# ###############################################################################################

# ## 비교 연산자###
# a = 10
# b = 20

# print(a < b)        # 10 < 20   = true
# print(a <= b)       # 10 <= 20  = true
# print(a > b)        # 10 > 20   = false
# print(a >= b)       # 10 >= 20  = false
# print(a == b)       # 10 == 20  = false
# print(a != b)       # 10 과 20은 같지 않다      = true

# # 논리형 자료 비교 #
# is_true = True      # ' 1 '을 의미함
# is_false = False    # ' 0 '을 의미함

# print(is_true > is_false)       # 1 > 0  => true
# print(is_true < is_false)       # 1 < 0  => false


# 문자형 자료 비교 #

# print("Python" > "pyhton")      # 대문자가 소문자보다 값이 작기때문에 false를 반환한다.
# print("123456" > "123455")      # 문자열이지만 숫자열을 비교하여 값을 주어 true를 반환한다.
# print("12.12" > "13.12")        # 문자열이지만 숫자열을 비교하여 값을 주어 false를 반환한다.


# ###############################################################################################

# ## 복합대입 연산자 ###
# # 1. 산술 연산자와 대입 연산자를 합쳐서 사용하는 것을 말함.
# 2. 신술 연산자 :  + - * / ** // %
# 3. 대입 연산자 : =
# # 4. 복합대입 연산자 : +=, -=, *=, /=, **=

# today = 1230
# today +=1
# print(today)
# 긴 코드를 축약해서 가독성을 높일 수 있음


# ###############################################################################################

# ## 논리연산자 ###
# bool자료형은 True와 False만 결과값을 가질수 있음.
# 그리고 비교값을 가지고도 결과값을 가질수 있었음.



# 1. and 연산
#     - and 값은 2값 모두 True 일경우 True를 반환해 줌
# print(True and True)    # 양쪽의 값이 모두 참일 경우만 True를 반환해 줌
# print(True and True)    # 한쪽이라도 거짓이 있을경우 False를 반환해 줌
# print(10>3 and 3<5)     # 수식에서도 사용 가능
# print(10==1 and 1==5)   # 양쪽 모두 거짓이면 당연히 False를 반환함.

# 다중 and연산을 사용할 경우
# 거짓으로 판별되는 가장첫번째 결과가 반환됨
# 모든항이 참인 결과값을 갖게 되면 마지막 값이 반환됨


# 2. or 연산
#     - 연산 값 중 한쪽이라도 True가 있다면 True 값을 반환해 줌
# print(True or False)       # 한쪽만 True여도 결과는 True를 반환함.
# print(False or True)       # 앞쪽에 False가 있어도 결과는 바뀌지 않는다.
# print(False or False)      # 둘다 False인 경우는 False 이다.

# 다중 or연산
# 참으로 판별되는 첫번째 값이 반환이됨.
# 모든결과가 거짓인 경우에는 마지막결과가 출력이 됨.

# 3. and, or 의 동일 연산
# and연산은 or 연산보다 우선순위가 높음.
# print(True or False and "참")       # 결과로 True를 반환함.
#                                     # False and "참"을 먼저 반환(false가 반환)하고, 그 반환값(false)을 True와 or 한다.
#                                     # 최종결과 True or False로 true가 1개 이상으로 True가 반환된다.

# print((True or False) and "참")
# # 연산의 우선순위를 정해주고 싶은경우는 ()로 지정해 주면 우선 시행된다.
# # 위 연산의 경우 True and "참"으로 둘다 True로 인해서 마지막 True인 "참"을 결과로 추출한다.


# # 4. not 연산자
# # 간단하게 참을 거짓으로, 거짓을 참으로 바꿔주는 연산자이다.
# print(not(True or False and "참"))
# print(not(True or False) and "참")


