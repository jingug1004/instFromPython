s1 = set([1, 2, 3])
print(s1)
# {1, 2, 3}

s2 = set("Hello")
print(s2)
# {'o', 'e', 'H', 'l'}

l1 = list(s1)
print(l1)
# [1, 2, 3]
print(l1[0])
# 1

t1 = tuple(s1)
print(t1)
# (1, 2, 3)

print(t1[0])
# 1

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

교집합 = s1 & s2
print(교집합)
# {4, 5, 6}
교집합02 = s1.intersection(s2)
print(교집합02)
# {4, 5, 6}

합집합 = s1 | s2
print(합집합)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
합집합02 = s1.union(s2)
print(합집합02)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

차집합 = s1 - s2
print(차집합)
# {1, 2, 3}
차집합02 = s2 - s1
print(차집합02)
# {8, 9, 7}

차집합03 = s1.difference(s2)
print(차집합03)
# {1, 2, 3}
차집합04 = s2.difference(s1)
print(차집합04)
# {8, 9, 7}

값1개추가하기 = set([1, 2, 3])
값1개추가하기.add(4)
print(값1개추가하기)
# {1, 2, 3, 4}

값여러개추가하기 = set([1, 2, 3])
값여러개추가하기.update([4, 5, 6])
print(값여러개추가하기)
# {1, 2, 3, 4, 5, 6}

특정값제거하기 = set([1, 2, 3])
특정값제거하기.remove(2)
print(특정값제거하기)
# {1, 3}