a = [1, 2, 3]
print(a)
b2 = a[0]
print(b2)
c3 = a[0] + a[2]
print(c3)
d4 = a[-1]
print(d4)
# [1, 2, 3]
# 1
# 4
# 3

a = [1, 2, 3, ['a', 'b', 'c']]
b2 = a[0]
print(b2)
c3 = a[-1]
print(c3)
d4 = a[3]
print(d4)
e5 = a[-1][0]
print(e5)
f6 = a[-1][1]
print(f6)
g7 = a[-1][2]
print(g7)
# 1
# ['a', 'b', 'c']
# ['a', 'b', 'c']
# a
# b
# c

a = [1, 2, ['a', 'b', ['Life', 'is']]]
b2 = a[2][2][0]
print(b2)
# Life

a = [1, 2, 3, 4, 5]
b2 = a[0:2]
print(b2)
# [1, 2]

aa = "12345"
bb22 = aa[0:2]
print(bb22)
# 12

b3 = a[:2]
print(b3)
c3 = a[2:]
print(c3)
# [1, 2]
# [3, 4, 5]

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
b4 = a[2:5]
print(b4)
c4 = a[3][:2]
print(c4)
# [3, ['a', 'b', 'c'], 4]
# ['a', 'b']

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
d = a * 3
print(d)
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 1, 2, 3, 1, 2, 3]

e = str(a[2]) + "Hi"
print(e)
# 3Hi

a = [1, 2, 3]
a[2] = 4
print(a)
# [1, 2, 4]

b = a[1:2]
print(b)
# [2]

a[1:2] = ['a', 'b', 'c']
print(a)
# [1, 'a', 'b', 'c', 4]

a[1:3] = []
print(a)
# [1, 'c', 4]

del a[1]
print(a)
# [1, 4]








