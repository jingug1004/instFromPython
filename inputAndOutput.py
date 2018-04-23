def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result = sum_many(1, 2, 3)
print(result)
# 6

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)
# 55

def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = sum_mul("sum", 1, 2, 3, 4, 5)
print(result)
# 15

result = sum_mul("mul", 1, 2, 3, 4, 5)
print(result)
# 120

def sum_and_mul(a, b):
    return a+b, a*b

result = sum_and_mul(3, 4)
print(result)
# (7, 12)

sum, mull = sum_and_mul(3, 4)
print(sum)
# 7
print(mull)
# 12

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
# 나의 이름은 박응용입니다.
# 나이는 27살 입니다.
# 남자입니다.

say_myself("박응용", 27, True)
# 나의 이름은 박응용입니다.
# 나이는 27살 입니다.
# 남자입니다.

say_myself("박응용", 27, False)
# 나의 이름은 박응용입니다.
# 나이는 27살 입니다.
# 여자입니다.

a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)
# 2

a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)
# 2

number = input("숫자를 입력하세요.")
print(number)
# 숫자를 입력하세요.3
# 3

print("life" "is" "short")
print("life" + "is" + "short")
# lifeisshort
# lifeisshort

print("life", "is", "short")
# life is short

for i in range(10):
    print(i, end='   ')
# 0   1   2   3   4   5   6   7   8   9





