text = "www.google.com"

### 내장함수 ###
# [표기법] : 내장함수(인자)

# len()
# len() 문자열의 길이를 반환해주는 함수
print(len(text))  # 14를 출력해줌

# .capitalize()
# .capitalize() 첫 문자를 대문자로 만들어줌, 나머지는 소문자
text_capitalize = text.capitalize()
print(text_capitalize)  # Www.google.com를 출력해줌

# .upper()
txt_upper = text.upper() # 문자열 전체를 대문자로 변경
print(txt_upper) # WWW.GOOGLE.COM 로 출력

# .lower()
txt_lower = text.lower() # 문자열 전체를 소문자로 변경
print(txt_lower) # www.google.com 로 출력

# count(a)
# (a)의 a에 찾고 싶은 문자/문자열 를 넣는다.
g_count = text.count('g')  # text에 'g'가 포함된 횟수를 반환한다.
print(g_count) # 2를 반환

# find(a)
# (a)의 a에 찾고 싶은 문자/문자열을 넣는다.
# 실행을 하게되면 찾고 싶은 문자/문자열이 n번째 있다는 것을 반환한다.
g_find = text.find('g')
print(g_find) # 4를 반환 / 5번째 g가 있음
g_find = text.find('g',5) # ('g',5)로 넣게되면, 5번 인덱스 부터 확인하겠다는 의미임
print(g_find)

# rfind, rindex처럼 앞에 r을 붙일경우 뒤에서부터 계산한다.

# index(a)
# 두 함수 모두 찾는 문자의 인덱스를 반환한다
# find와 index의 경우는 오류를 반환한다.

# replace()
# 문자열을 치환해 주는 메서드
# [표현법] replace(현재 문자/문자열, 변경 문자/문자열)
text_naver = text.replace("google", "naver")
print(text_naver)  # => www.naver.com

# split()
# ()에 넣어주는 인자값에 따라서 분리해주는 메서드
print(text.split('.'))  # => ['www', 'google', 'com']
# '.'을 기준으로 나눠줌

# strip()
# 공백을 지워주는 메서드
# 주의사항 공백이 문자열 사이사이에 들어 있을경우 지워지지 않음
# 문자열 양끝에 있는 공백만 지워줌
stp = text.strip()






