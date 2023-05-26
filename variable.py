#변수 선언#
#기본문법 
a = 100     # 참조할 값을 변수에 할당
print(a)    # 100이라는 값을 출력함
b = 200
print(b)



#선언한 변수를 지울때#
#기본 문법 : del 변수명     ex) del a
c = 100     # c변수를 100으로 선언
del c       # c변수를 del로 지움
print(c)    # NameError: name 'b' is not defined
            # 변수 b를 선언하지 않았다는 의미
          

#200 = b
#print(b) #SyntaxError: cannot assign to literal here.
         #      Maybe you meant '==' instead of '='?
         # 구문 오류가 발생

