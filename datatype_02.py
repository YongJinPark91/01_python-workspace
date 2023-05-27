# 문자열 데이터 String #

text_1 = "String Data Type" 
text_2 = 'String Data Type' # ""와 ''의 표기 차이는 없음

text_3 = 'String "Data" Type' # ''안에 "" 를 사용하여 표현할 수 있음
#print(text_3)
text_4 = "String \"Data\" Type" # 탈출문자를 활용한 출력
#print(text_4)
#탈출문자
#종류 : \' , \" , \\ , \n , \r , \t
# 예문 : "Python is Easy"

# 1. \' , \"
text1_1 = "Python \'is\" Easy"
# print(text1_1) => Python 'is" Easy 가 출력

# 2. \\
text1_2 = "Python \\is\\ Easy"
#print(text1_2) => Python \is\ Easy
# Tip
# ' \ ' 하나만 쓴 경우는 로직이 길어졌을때 가독성을
#       높이기 위해서 사용하는 경우
# a = "123456789\
# abcdefghijk"
# print(a)    // 123456789 abcdefghijk 정상출력

# 3. \n
# 개행의 의미로 다음 줄로 넘겨줌
text1_3 = "Python \nis Easy"
# Python 
# is Easy 이 2줄로 출력됨
#print(text1_3)

# 4. \r
# \r 의 다음부분부터 출력이 됨
text1_4 = "Python \r is Easy"
#print(text1_4)

# 5.''' / """"
# '''(""")내용'''을 하면 띄우거나 개행을 쓸수 있다
text1_5 = """홍길동
김유신
강감찬"""
#print(text1_5)

# 6. 문자열 간의 연산
text2_1 = "Python is Easy"
text2_2 = "and Powerful"

print(text2_1 + text2_2) # text 2_1과 2_2를 더해서 출력한다.
print(text2_1 * 3)       # text 2_1을 연속으로 세번 출력한다



