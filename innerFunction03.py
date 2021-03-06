def 입력받은자료형의각요소가함수f에의해수행된결과를묶어서리턴01(x) : return x * 2
print(list(map(입력받은자료형의각요소가함수f에의해수행된결과를묶어서리턴01, [1, 2, 3, 4])))
# [2, 4, 6, 8]

print(list(map(lambda  a : a * 2, [1, 2, 3, 4])))
# [2, 4, 6, 8]

def 입력받은자료형의각요소가함수f에의해수행된결과를묶어서리턴02(x):
    return x + 1
print(list((map(입력받은자료형의각요소가함수f에의해수행된결과를묶어서리턴02, [1, 2, 3, 4]))))
# [2, 3, 4, 5]

인수로반복가능한자료형을입력받아그최대값을리턴하는함수01 = max([1, 2, 3])
print(인수로반복가능한자료형을입력받아그최대값을리턴하는함수01)
# 3
인수로반복가능한자료형을입력받아그최대값을리턴하는함수02 = max("python")
print(인수로반복가능한자료형을입력받아그최대값을리턴하는함수02)
# y

인수로반복가능한자료형을입력받아그최소값을리턴하는함수01 = min([1, 2, 3])
print(인수로반복가능한자료형을입력받아그최소값을리턴하는함수01)
# 1
인수로반복가능한자료형을입력받아그최소값을리턴하는함수02 = min("python")
print(인수로반복가능한자료형을입력받아그최소값을리턴하는함수02)
# h

정수형태의숫자를8진수문자열로바꾸어리턴01 = oct(34)
print(정수형태의숫자를8진수문자열로바꾸어리턴01)
# 0o42
정수형태의숫자를8진수문자열로바꾸어리턴02 = oct(12345)
print(정수형태의숫자를8진수문자열로바꾸어리턴02)
# 0o30071

문자의아스키코드값을리턴01 = ord('a')
print(문자의아스키코드값을리턴01)
# 97
문자의아스키코드값을리턴02 = ord('0')
print(문자의아스키코드값을리턴02)
# 48

x의y제곱한결과값을리턴01 = pow(2, 4)
print(x의y제곱한결과값을리턴01)
# 16
x의y제곱한결과값을리턴02 = pow(3, 3)
print(x의y제곱한결과값을리턴02)
# 27

입력받은숫자에해당되는범위의값을반복가능한객체01 = list(range(5))
print(입력받은숫자에해당되는범위의값을반복가능한객체01)
# [0, 1, 2, 3, 4]
입력받은숫자에해당되는범위의값을반복가능한객체02 = list(range(5, 10))
print(입력받은숫자에해당되는범위의값을반복가능한객체02)
# [5, 6, 7, 8, 9]
입력받은숫자에해당되는범위의값을반복가능한객체03 = list(range(1, 10, 2))
print(입력받은숫자에해당되는범위의값을반복가능한객체03)
# [1, 3, 5, 7, 9]
입력받은숫자에해당되는범위의값을반복가능한객체04 = list(range(0, -10, -1))
print(입력받은숫자에해당되는범위의값을반복가능한객체04)
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

입력값을정렬한후그결과를리스트로리턴01 = sorted([3, 1, 2])
print(입력값을정렬한후그결과를리스트로리턴01)
# [1, 2, 3]
입력값을정렬한후그결과를리스트로리턴02 = sorted(['a', 'c', 'b'])
print(입력값을정렬한후그결과를리스트로리턴02)
# ['a', 'b', 'c']
입력값을정렬한후그결과를리스트로리턴03 = sorted("zero")
print(입력값을정렬한후그결과를리스트로리턴03)
# ['e', 'o', 'r', 'z']
입력값을정렬한후그결과를리스트로리턴04 = sorted((3, 2, 1))
print(입력값을정렬한후그결과를리스트로리턴04)
# [1, 2, 3]

문자열형태로객체를변환하여리턴01 = str(3)
print(문자열형태로객체를변환하여리턴01)
# 3
문자열형태로객체를변환하여리턴02 = str('hi')
print(문자열형태로객체를변환하여리턴02)
# hi
문자열형태로객체를변환하여리턴03 = str('hi'.upper())
print(문자열형태로객체를변환하여리턴03)
# HI

반복가능한자료형을입력받아튜플형태로바꾸어리턴01 = tuple("abc")
print(반복가능한자료형을입력받아튜플형태로바꾸어리턴01)
# ('a', 'b', 'c')
반복가능한자료형을입력받아튜플형태로바꾸어리턴02 = tuple([1, 2, 3])
print(반복가능한자료형을입력받아튜플형태로바꾸어리턴02)
# (1, 2, 3)
반복가능한자료형을입력받아튜플형태로바꾸어리턴03 = tuple((1, 2, 3))
print(반복가능한자료형을입력받아튜플형태로바꾸어리턴03)
# (1, 2, 3)

입력값의자료형이무엇인지알려줌01 = type("abc")
print(입력값의자료형이무엇인지알려줌01)
# <class 'str'>
입력값의자료형이무엇인지알려줌02 = type([])
print(입력값의자료형이무엇인지알려줌02)
# <class 'list'>
입력값의자료형이무엇인지알려줌03 = type(open("test", 'w'))
print(입력값의자료형이무엇인지알려줌03)
# <class '_io.TextIOWrapper'>

동일한개수로이루어진자료형을묶어주는역할01 = list(zip([1, 2, 3], [4, 5, 6]))
print(동일한개수로이루어진자료형을묶어주는역할01)
# [(1, 4), (2, 5), (3, 6)]
동일한개수로이루어진자료형을묶어주는역할02 = list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(동일한개수로이루어진자료형을묶어주는역할02)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
동일한개수로이루어진자료형을묶어주는역할03 = list(zip("abc", "def"))
print(동일한개수로이루어진자료형을묶어주는역할03)
# [('a', 'd'), ('b', 'e'), ('c', 'f')]