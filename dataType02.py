a = "hobby"
문자개수세기 = a.count('b')
print(문자개수세기)
# 2

a = "Python is best choice"
위치알려주기01 = a.find('b')
print(위치알려주기01)
위치알려주기02 = a.find('k')
print(위치알려주기02)
# 2
# 10
# -1

a = "Life is too short"
위치알려주기03 = a.index('t')
print(위치알려주기03)
# 위치알려주기04 = a.index('k')
# print(위치알려주기04)
# 2
# Traceback (most recent call last):
# 10
# -1
# File "C:/Python/dataType02.py", line 18, in <module>
# 위치알려주기04 = a.index('k')
# 8
# ValueError: substring not found

a = ","
문자열삽입 = a.join('abcd')
print(문자열삽입)
# 2
# 10
# -1
# 8
# a,b,c,d

a = "Hi, Hello"
소문자를대문자로바꾸기 = a.upper()
print(소문자를대문자로바꾸기)
a = "Hi, Hello"
대문자를소문자로바꾸기 = a.lower()
print(대문자를소문자로바꾸기)
# 2
# 10
# -1
# 8
# a,b,c,d
# HI, HELLO
# hi, hello

a = "   Hi, Hello     "
왼쪽공백지우기 = a.lstrip()
print(왼쪽공백지우기)
a = "   Hi, Hello     "
오른쪽공백지우기 = a.rstrip()
print(오른쪽공백지우기)
a = "   Hi, Hello     "
양쪽공백지우기 = a.strip()
print(양쪽공백지우기)
# 2
# 10
# -1
# 8
# a,b,c,d
# HI, HELLO
# hi, hello
# Hi, Hello
#   Hi, Hello
# Hi, Hello

a = "Life is too short"
문자열바꾸기 = a.replace("Life", "Your leg")
print(문자열바꾸기)
b = "Life is too short"
문자열나누기01 = b.split()
print(문자열나누기01)
c = "a:b:c:d"
문자열나누기02 = c.split(":")
print(문자열나누기02)
# 2
# 10
# -1
# 8
# a,b,c,d
# HI, HELLO
# hi, hello
# Hi, Hello
#     Hi, Hello
# Hi, Hello
# Your leg is too short
# ['Life', 'is', 'too', 'short']
# ['a', 'b', 'c', 'd']
