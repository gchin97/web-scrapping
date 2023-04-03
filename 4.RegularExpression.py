import re
# 패턴 값을 받아옴
p = re.compile("ca.e")  # .은 하나의 문자를 의미함
# ^: 문자열의 시작을 의미함 ex, de : desk, decomposition
# $: 문자열의 끝을 의미 ex, case, base
m = p.match("case")
print(m.group())  # .group() 매칭되는지 찾아주는 함수


def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")


m = p.match("careless")  # 주어진 문자열이 처음부터 일치하는지 확인

print_match(m)
