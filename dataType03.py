숫자바로대입하기 = "I eat {0} apples".format(1)
print(숫자바로대입하기)
# I eat 1 apples

문자열바로대입하기 = "I eat {0} apples".format("two")
print(문자열바로대입하기)
# I eat 1 apples
# I eat two apples

number = 3
숫자값을가진변수로대입하기 = "I eat {0} apples".format(number)
print(숫자값을가진변수로대입하기)
# I eat 1 apples
# I eat two apples
# I eat 3 apples

number = 4
day = "five"
두개이상의값넣기 = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(두개이상의값넣기)
# I eat 1 apples
# I eat two apples
# I eat 3 apples
# I ate 4 apples. so I was sick for five days.

이름으로넣기 = "I ate {number} apples. so I was sick for {day} days.".format(number=6, day=7)
print(이름으로넣기)
# I eat 1 apples
# I eat two apples
# I eat 3 apples
# I ate 4 apples. so I was sick for five days.
# I ate 6 apples. so I was sick for 7 days.

인덱스와이름을혼용해서넣기 = "I ate {0} apples. so I was sick for {day} days.".format(8, day=9)
print(인덱스와이름을혼용해서넣기)
# I eat 1 apples
# I eat two apples
# I eat 3 apples
# I ate 4 apples. so I was sick for five days.
# I ate 6 apples. so I was sick for 7 days.
# I ate 8 apples. so I was sick for 9 days.

왼쪽정렬 = "{0:<10}" .format("Hi")
print(왼쪽정렬)
오른쪽정렬 = "{0:>10}" .format("Hi")
print(오른쪽정렬)
가운데정렬 = "{0:^10}" .format("Hi")
print(가운데정렬)
# I eat 1 apples
# I eat two apples
# I eat 3 apples
# I ate 4 apples. so I was sick for five days.
# I ate 6 apples. so I was sick for 7 days.
# I ate 8 apples. so I was sick for 9 days.
# Hi
#         Hi
#     Hi

공백채우기01 = "{0:=^10}" .format("Hi")
공백채우기02 = "{0:!<10}" .format("Hi")
print(공백채우기01)
print(공백채우기02)
# I eat 1 apples
# I eat two apples
# I eat 3 apples
# I ate 4 apples. so I was sick for five days.
# I ate 6 apples. so I was sick for 7 days.
# I ate 8 apples. so I was sick for 9 days.
# Hi
#         Hi
#     Hi
# ====Hi====
# Hi!!!!!!!!

y = 3.42134234
소수점표현하기01 = "{0:0.4f}" .format(y)
print(소수점표현하기01)
소수점표현하기02 = "{0:10.4f}" .format(y)
print(소수점표현하기02)
# I eat 1 apples
# I eat two apples
# I eat 3 apples
# I ate 4 apples. so I was sick for five days.
# I ate 6 apples. so I was sick for 7 days.
# I ate 8 apples. so I was sick for 9 days.
# Hi
#         Hi
#     Hi
# ====Hi====
# Hi!!!!!!!!
# 3.4213
#     3.4213

중괄호문자표현하기 = "{{and}}" .format()
print(중괄호문자표현하기)
# I eat 1 apples
# I eat two apples
# I eat 3 apples
# I ate 4 apples. so I was sick for five days.
# I ate 6 apples. so I was sick for 7 days.
# I ate 8 apples. so I was sick for 9 days.
# Hi
#         Hi
#     Hi
# ====Hi====
# Hi!!!!!!!!
# 3.4213
#     3.4213
# {and}

