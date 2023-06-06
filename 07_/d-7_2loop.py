"""
i = 0

while True :
    print("{}번째 반복입니다.".format(i))45
    i += 1
    if i > 10:
        break
"""

sum = 0

while True :
    num = int(input("정수를 입력하세요(0입력시 종료)"))
    if(num == 0):
        break
        if(num % 2 ==0):
            sum += num
            print("현재 정수의 합은 {}입니다.".format(sum))
        else :
            print("짝수가 아닙니다.")