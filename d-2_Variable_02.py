#문자열 출력#
text = "Hello World!"       # text라는 변수에 문자열 Hello World! 대입
                            # 변수를 쓸경우 변수에 대입된 문자열만 바꿔줘도 한번에 변경이 가능하다
print((text + "\n") * 10)   # text 변수를 통해서 다회 출력, ' \n '은 개행의 의미


#연습문제#
#이름, 핸드폰번호, 거주지 를 출력하자.
name = "홍길동"
phone_number = "010-1234-5678"      # 파이썬은 기본적으로 8진수를 쓰는데 전화번호는 10진수의 형식을 따름
                                    # 그래서 ""를 붙여서 문자열로 인식하게 하여 출력하는 것이 올바른 표기법임
address = "서울시 용산구"

print(name)
print(phone_number)
print(address)
