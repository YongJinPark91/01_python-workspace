# [표현법]
# if 조건식 A : 
#     조건식 A가 참일 때 실행할 문장
# elif 조건식 B : 
#     조건식 B가 참일 때 실행할 문장
# elif 조건식 C : 
#     조건식 C가 참일 때 실행할 문장
# else :
#     모든조건식이 거짓일 때 실행할 문장
"""
[예시1]
lunch = input("점심메뉴를 골라주세요(제육덮밥, 김밥, 돈까스)")
if lunch == "제육덮밥" :
    print("제육덮밥 먹는다")
elif lunch == "돈까스" :
    print("돈까스를 먹는다")
elif lunch == "김밥" :
    print("김밥을 먹는다")
else:
    print("점심을 굶는다")
"""

"""
number = int(input("숫자를 하나 입력해 주세요"))
if number > 50 :
    print("50보다 큰 수입니다.")
elif number > 80:
    print("90보다 작고 80보다 큰수입니다")
elif number > 90:
    print("80보다 작고 50보다 큰수입니다")
else:
    print("50보다 작은수 입니다.")
"""
"""
# 3의 배수이면서 짝수인지 판별해주는 조건식
num = int(input("정수를 입력해주세요."))
if num % 3 == 0 and num % 2 == 0 :
    print("3의 배수이면서 짝수 입니다")
elif num % 3 ==0 :
    print("3의 배수 입니다.")
elif num % 2 !=0 :
    print("3의 배수 또는 짝수가 아닙니다")
"""
# 웹사이트 판별 하기
www = input("도메인 주소 입력 : ")
i = www.split('.')
print(i[-1])
if i == "kr" :
    print("한국")
elif i == "uk" :
    print("영국")
elif i == "com" :
    print("기업")
elif i == "org" :
    print("기업")
else :
    print("그 외 사이트 입니다.")

# .kr 한국 / .uk 영국 / .com 기관 / .org