###식별자 생성 규칙###
# 올바른 예
apple = "사과"
apples = "사과들"
apple3 = "사과3개"
app3le = "사3과"
app3le = "사3과"
red_apple = "빨간 사과"     # ' _ '를 사용한 표기법을 snake_case(뱀표기법) 이라고 하며, 2개 이상의 단어를 사용할 때 사용함
verydeliciousredapple = "아주 맛있는 빨간 사과"
very_delicious_red_apple = "아주 맛있는 빨간 사과"

# 올바르지 않은 예
#red apple = "빨간 사과"     # 오류 발생 : SyntaxError: invalid syntax
                            # 공백을 넣을 수 없다.
#3apple = "3개의 사과"       # 숫자가 먼저 올 수 없다.
#apple! = "사과!"            # ' _ '을 제외한 특수기호는 올 수 없다.
#continue =                  # 글자색이 보라색으로 변경되는 예약어는 사용할 수 없다.



