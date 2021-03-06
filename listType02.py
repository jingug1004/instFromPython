리스트에요소추가 = [1, 2, 3]
리스트에요소추가.append(4)
print(리스트에요소추가)
# [1, 2, 3, 4]
리스트에요소추가.append([5, 6])
print(리스트에요소추가)
# [1, 2, 3, 4, [5, 6]]

리스트정렬 = [1, 4, 3, 2]
리스트정렬.sort()
print(리스트정렬)
# [1, 2, 3, 4]
리스트정렬02 = ['a', 'c', 'b', 'bedd', '가', '나가', '가마', '9', '1']
리스트정렬02.sort()
print(리스트정렬02)
# ['a', 'b', 'c']
# ['1', '9', 'a', 'b', 'bedd', 'c', '가', '가마', '나가']

리스트뒤집기 = ['a', 'c', 'b', 'bedd', '가', '나가', '가마', '9', '1']
리스트뒤집기.reverse()
print(리스트뒤집기)
# ['1', '9', '가마', '나가', '가', 'bedd', 'b', 'c', 'a']

위치반환 = [1, 2, 3]
b = 위치반환.index(3)
c = 위치반환.index(1)
# d = 위치반환.index(4)
print(b)
print(c)
# print(d)
# 2
# 0
# ValueError: 4 is not in list d = 위치반환.index(4)

리스트에요소삽입 = [1, 2, 3]
리스트에요소삽입.insert(0, 4)
print(리스트에요소삽입)
# [4, 1, 2, 3]
리스트에요소삽입.insert(3, 5)
print(리스트에요소삽입)
# [4, 1, 2, 5, 3]
리스트에요소삽입.insert(9, 9)
print(리스트에요소삽입)
# [4, 1, 2, 5, 3, 9]

리스트요소제거 = [1, 2, 3, 1, 2, 3]
리스트요소제거.remove(3)
print(리스트요소제거)
# [1, 2, 1, 2, 3]
# 리스트요소제거.remove(9)
# print(리스트요소제거)
# ValueError: list.remove(x): x not in list 리스트요소제거.remove(9)

리스트요소끄집어내기 = [1, 2, 3]
리스트요소끄집어내기.pop()
print(리스트요소끄집어내기)
# [1, 2]

리스트요소끄집어내기02 = [1, 2, 3]
리스트요소끄집어내기02.pop(1)
print(리스트요소끄집어내기02)
# [1, 3]

리스트에포함된요소의개수세기 = [1, 2, 3, 1]
bb = 리스트에포함된요소의개수세기.count(1)
print(bb)
# 2

리스트확장01 = [1, 2, 3]
리스트확장01.extend([4, 5])
print(리스트확장01)
# [1, 2, 3, 4, 5]
리스트확장02 = [6, 7]
리스트확장01.extend(리스트확장02)
print(리스트확장01)
# [1, 2, 3, 4, 5, 6, 7]
