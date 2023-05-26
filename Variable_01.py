#변수 선언#
#기본문법 : 변수 = 참조값
a = 100     # 참조할 값을 변수에 할당
print(a)    # 100이라는 값을 출력함

#100 = a    # 좌항과 우항이 바뀌어서는 안됨
#print(b)   #SyntaxError: cannot assign to literal here.
            #      Maybe you meant '==' instead of '='?
            # 구문 오류가 발생
b = 200
print(b)

#선언한 변수를 지울때#
#기본 문법 : del 변수명     ex) del a
c = 100     # 변수'c'를 100으로 선언
#del c      # 변수'c'를 'del'로 지움
print(c)    # NameError: name 'b' is not defined
            # 변수 b를 선언하지 않았다는 의미

#변수의 동시 선언#
d, e = 100, 200     # d, e를 좌항에 선언하면서 우항에 100과 200을 넣어주었음
                    # 그러나 d가 무조건 100이 되거나, e가 무조건 200이 되지는 않음.

#값의 할당#                    
#d = e          # d에 e의 200의 값을 대입
                # d = 200, e = 200 이 된다
d, e = e, d+e   # 위와 같은 형태라면 d = e, e = e(앞에 d = e)+e 가 들어 갈 것 같지만
                # 실제 런을 하면  d, e = 200, 300이 출력된다

#연산자의 우선순위#
# ' + ' 연산자는 ' = ' 연산자 보다 우선순위가 높다
# d+e를 먼서 수행 후 d에 e를 대입한다.

print(d)
print(e)

#동시 출력#
print(d, e)  # print(d), print(e)를 따로 한 것과 동일하게 나오지만 횡으로 출력됨


#======================문자열======================#
print("Hello World")

          


