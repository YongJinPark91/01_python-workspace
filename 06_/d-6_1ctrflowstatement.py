# input 함수
# text = input("성을 입력해주세요")
# text = input("이름을 입력해주세요")
# print(text)
##number = input("첫번째 정수를 입력해주세요>")
##number2 = input("두번째 정수를 입력해주세요>")

# print(number + number2) # 50, 30을 넣어 80의 값을 나타내고 싶지만, 실제는 5030으로 나타남
#80이라는 값을 출력하기 위해서는 자료형을 int 형으로 변환 시켜야 한다.
##print(int(number) + int(number2))

#만약 print 단계에서 형변환을 하지 않고 싶다면
# number = int(input("첫번째 정수를 입력해주세요>"))     // 질문 선언단계에서 자료형을 선정함
# number2 = float(input("두번째 정수를 입력해주세요>")) 

###########################################################################################

#if문
#기본형태
#   - if True(조건식) : 
#         print("실행할 문장입니다.") // 조건식이 참일경우 실행할 문장이옴, print 앞에 4칸을 띄워야함.
#if True :
#    print("실행할 문장입니다.")
#    print("똑같이 실행할 문장입니다.")

# weather = input("오늘의 날씨를 입력해 주세요")    
# if weather == "비" :
#     print("우산을 챙겨나가세요")

time = int(input("파이썬 공부 가능한 시간"))
if time > 4 :
    print("열심히 공부해야지")