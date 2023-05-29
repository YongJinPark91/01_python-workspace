weather = "맑음"
temperature = 20
chance_shower = 33.5

# 데이터 타입 선언
print("{0:s}, {1:d}, {1:f}, {1:o}, {1:x}".format(weather, temperature))
#  s:문자 / d:정수형 / f:실수형 / o:8진수 / x:16진수

# 문자열과 함수를 같이 쓰는 경우 (가능한 타입 3가지)
#1 ','를 활용한 방법
print("오늘의 날씨는", weather, "기온은", temperature, "도 입니다.")
# print("오늘의 날씨는"+ weather+ "기온은"+ temperature+ "도 입니다.")
# ','가 아니라 '+'를 쓰는 경우 문자열과 정수형은 +할 수 없다.

print("===========구분선===========")

#2 %를 활용한 방법
print("오늘의 날씨는 %s 기온은 %d도 입니다." % (weather, temperature))
    # 권장하지는 않는 방법, 요소들의 순서가 변하지 않고 일반적일 경우만 가능
print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %d%%입니다." % (weather, temperature,chance_shower))
    # 명확한 타입을 모르게되면 타입에러가 생길 확률이 높음
    # 위의 비가올 확률은 실수로서 타입의 작성을 잘해야 에러가 발생하지 않음

print("===========구분선===========")

#3 {}, .format()을 활용한 방법
# [표현법 1] : print("내용 {} 내용 {}".format(0번 변수명, 1번 변수명))
#               {}안에 공백으로 둘 경우 순서대로 가져옴
print("오늘의 날씨는 {} 기온은 {}도 비가내릴 확률은 {}입니다.".format(weather, temperature,chance_shower))
#  => 오늘의 날씨는 맑음 기온은 20도 비가내릴 확률은 33.5입니다.

# [표현법 2] : print("내용 {n번} 내용 {n번}".format(0번 변수명, 1번 변수명))
#               {}안에 .format(0번째, 1번째) 둘중 원하는 번째의 숫자를 넣어주면 대입이 됨
print("오늘의 날씨는 {0} 기온은 {2}도 비가내릴 확률은 {1}입니다.".format(weather, temperature,chance_shower))
#  => 오늘의 날씨는 맑음 기온은 33.5도 비가내릴 확률은 20입니다.

print("===========구분선===========")

#4 기타 특이사항
# 자리수 지정 : {n:m}에서 m을 원하는 숫자를 넣으면 m번 사이즈 만한 칸에 들어감
#               n은 format 변수 n번째를 뜻함
print("{:10},{:10}".format(weather, temperature))

# 정렬 : 숫자는 기본적으로 오른쪽 정렬, 문자는 왼쪽 정렬이 됨
print("{:10},{:10}".format(weather, temperature))
#  => 맑음        ,        20  출력
print("{1:10},{0:10}".format(weather, temperature))
#  =>         20,맑음  출력
# 정렬방법 변경하는법 : <(왼쪽정렬), >(오른쪽정렬), ^(가운데 정렬)
left = "left"
right = "right"
middle = "middle"
print("({:>10s}), ({:^10s}), ({:<10s})".format(left,middle, right))
#   (      left), (  middle  ), (right     ) // 출력됨
print("({:1>10s}), ({:1^10s}), ({:1<10s})".format(left,middle, right))
#    (111111left), (11middle11), (right11111) // 출력됨
# {:>10s}와 같이 출력하면 left의 칸을 제외한 나머지는 공백으로 출력된다.
# {:1>10s}와 같이 ' : ' 다음에 숫자, 문자를 입력해 주면 입력값으로 공백을 채운다.
print("({:1>10.2s}), ({:1^10.2s}), ({:1<10.2s})".format(left,middle, right))
# {:1>10s}에서 칸다음 ' .n '을 해주면 입력값 중 n개 만큼만 출력하고 나머지는 입력 갑으로 채움
#      (11111111le), (1111mi1111), (ri11111111) // 출력됨

print("===========구분선===========")

### f-string 활용 ###
# [표현법] : print(f"내용1 {변수1}, 내용2{변수2}.")
# 위 표현법들중 가장 직관적이고, 쉬운 표기법
# 수식의 결과도 표현할 수 있음

print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}도 입니다.")
print(f"2*3의 결과값{2*3}")