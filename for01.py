a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
# 3
# 7
# 11

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)
# 1번 학생 축하합니다. 합격입니다.
# 3번 학생 축하합니다. 합격입니다.
# 5번 학생 축하합니다. 합격입니다.

b = range(10)
print(b)
# range(0, 10)

c = range(1, 11)
print(c)
# range(1, 11)

sum = 0
for i in range(1, 11):
    sum = sum + i
    print(sum)
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55
print(sum)
# 55

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))
# 1번 학생 축하합니다. 합격입니다.
# 3번 학생 축하합니다. 합격입니다.
# 5번 학생 축하합니다. 합격입니다.

for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print()
# 2 4 6 8 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81

c = [1, 2, 3, 4]
result = []
for number in c:
    result.append(number * 3)
print(result)
# [3, 6, 9, 12]

result = [number * 3 for number in c if number % 2 == 0]
print(result)
# [6, 12]

result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
print(result)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21,
# 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20,
# 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54,
# 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40,
# 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
