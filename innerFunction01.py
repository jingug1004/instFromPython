절대값01 = abs(3)
절대값02 = abs(-3)
절대값03 = abs(-1.2)
print(절대값01)
print(절대값02)
print(절대값03)
# 3
# 3
# 1.2

반복가능한자료형01 = all([1, 2, 3])
반복가능한자료형02 = all([1, 2, 3, 0])
print(반복가능한자료형01)
print(반복가능한자료형02)
# True
# False

all의반대경우01 = any([1, 2, 3, 0])
all의반대경우02 = any([0, ""])
print(all의반대경우01)
print(all의반대경우02)
# True
# False

아스키코드로출력01 = chr(97)
아스키코드로출력02 = chr(48)
print(아스키코드로출력01)
print(아스키코드로출력02)
# a
# 0

객체가자체적으로가지고있는변수나함수01 = dir([1, 2, 3])
객체가자체적으로가지고있는변수나함수02 = dir({'1':'a'})
print(객체가자체적으로가지고있는변수나함수01)
print(객체가자체적으로가지고있는변수나함수02)
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']
# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
# '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
# 'pop', 'popitem', 'setdefault', 'update', 'values']

a를b로나눈몫과나머지를튜플형태로01 = divmod(7, 3)
a를b로나눈몫과나머지를튜플형태로02 = divmod(1.3, 0.2)
print(a를b로나눈몫과나머지를튜플형태로01)
print(a를b로나눈몫과나머지를튜플형태로02)
# (2, 1)
# (6.0, 0.09999999999999998)

# 순서가있는자료형 =
for 순서가있는자료형, name in enumerate(['body', 'foo', 'bar']):
    print(순서가있는자료형, name)
# 0 body
# 1 foo
# 2 bar

문자열을실행한결과값을리턴01 = eval('1 + 2 ')
문자열을실행한결과값을리턴02 = eval("'hi' + 'a'")
문자열을실행한결과값을리턴03 = eval('divmod(4, 3)')
print(문자열을실행한결과값을리턴01)
print(문자열을실행한결과값을리턴02)
print(문자열을실행한결과값을리턴03)
# 3
# hia
# (1, 1)

def 리턴값이참인것만묶어서돌려줌01(numberList):
    result = []
    for num in numberList:
        if num > 0:
            result.append(num)
    return result

print(리턴값이참인것만묶어서돌려줌01([1, -3, 2, 0, -5, 6]))
# [1, 2, 6]

def 리턴값이참인것만묶어서돌려줌02(x):
    return x > 0

print(list(filter(리턴값이참인것만묶어서돌려줌02, [1, -3, 2, 0, -5, 6])))
# [1, 2, 6]

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))
# [1, 2, 6]

a16진수변환01 = hex(234)
a16진수변환02 = hex(3)
print(a16진수변환01)
print(a16진수변환02)
# 0xea
# 0x3

aaa = 3
객체고유주소값레퍼런스리턴01 = id(3)
print(객체고유주소값레퍼런스리턴01)
# 1849156400
객체고유주소값레퍼런스리턴02 = id(aaa)
print(객체고유주소값레퍼런스리턴02)
# 1849156400
bbb = aaa
객체고유주소값레퍼런스리턴03 = id(bbb)
print(객체고유주소값레퍼런스리턴03)
# 1849156400