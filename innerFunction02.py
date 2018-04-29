# 사용자입력받는01 = input()
# print(사용자입력받는01)
# hi
# hi

# 사용자입력받는02 = input("Enter: ")
# print(사용자입력받는02)
# Enter: hi
# hi

정수형태로리턴01 = int('3')
정수형태로리턴02 = int(3.4)
print(정수형태로리턴01)
print(정수형태로리턴02)
# 3
# 3

a2진수로표현된 = int('11', 2)
a16진수로표현된 = int('1A', 16)
print(a2진수로표현된)
print(a16진수로표현된)
# 3
# 26

class Person: pass


aPerson = Person()
bPerson = 3
그클래스의인스턴스인지를판단01 = isinstance(aPerson, Person)
그클래스의인스턴스인지를판단02 = isinstance(bPerson, Person)
print(그클래스의인스턴스인지를판단01)
print(그클래스의인스턴스인지를판단02)
# True
# False

람다01 = lambda a, b: a + b
print(람다01(3, 4))
# 7

람다02 = [lambda a, b: a + b, lambda a, b: a * b]
print(람다02)
# [<function <lambda> at 0x00663780>, <function <lambda> at 0x00663738>]

print(람다02[0])
# <function <lambda> at 0x02533780>
print(람다02[0](3, 4))
# 7
print(람다02[1](3, 4))
# 12

입력값길이리턴01 = len("python")
입력값길이리턴02 = len([1, 2, 3])
입력값길이리턴03 = len((1, 'a'))
print(입력값길이리턴01)
print(입력값길이리턴02)
print(입력값길이리턴03)
# 6
# 3
# 2

리스트로만들어리턴01 = list("python")
리스트로만들어리턴02 = list("python")
리스트로만들어리턴03 = [1, 2, 3]
print(리스트로만들어리턴01)
print(리스트로만들어리턴02)
print(list(리스트로만들어리턴03))
# ['p', 'y', 't', 'h', 'o', 'n']
# [1, 2, 3]
# [1, 2, 3]





