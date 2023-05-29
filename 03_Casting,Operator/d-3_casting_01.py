### 형 변환 ###


### int() 정수형
# 실수형, 논리형, 문자열
# 기본문법 : (변경을 원하는 자료형 (변경전 자료))
#        ex) print (int (123.92)) => 123


## 실수형
print(int(123.92456465))    # 123을 정수로 받는다.
print(int(123.0))           # 123을 정수로 받는다.

## 논리형
print(int(True))            # boolean 형태를 정수로 변경 => 1 
print(int(False))           # boolean 형태를 정수로 변경 => 0

## 문자열
print(int("123456789"))     # ""를 주어 String 형태도 정수형태로 변경
#단. 문자열을 정수형으로 변경할 때 다른문자가 들어있으면 변환이 되지 않음.
#print(int("123456789a"))   # ""내에 숫자 외 'a'가 들어있어서 제한됨.



############################################################################################################

### float() 실수형
# 정수형, 논리형, 문자열(특수한 형태도 일부가능)

## 정수형
print(float(200))           # 내용은 정수이지만 실수형타입으로 변경하여 출력을 하게되면 200.0을 반환한다.
print(float(3))             # 위와 동일하게 정수이지만 3.0으로 출력된다.

## 논리형 
print(float(True))          # 1.0으로 변환됨.
print(float(False))         # 0.0으로 변환됨.

## 문자열
# 문자열 안에 실수/정수형의 자료형태로 구성이 되어 있다면 가능
print(float("23.123456"))   # 실수형으로 변환가능
print(float("123"))



############################################################################################################

### str() 문자열
# 모든자료형을 문자열로 변경가능

print(str(123123132))
print(str(123.12312))
print(str(True))
print(str(False))


############################################################################################################


### bool() 논리자료형
# 모든 자료형을 논리형태로 변경가능

##False
# 0, 공백인 상태는 'f'를 반환함
print(bool(0))
print(bool(0.0))
print(bool(""))

##True
# false를 제외한 나머지 형태는 모둡 't'를 반환함.
print(bool(1))
print(bool(1.0))
print(bool("str"))
print(bool("1231"))
