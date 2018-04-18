a = {1: 'a'}
a[2] = 'b'
print(a)
# {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a)
# {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1, 2, 3]
print(a)
# {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

del a[1]
print(a)
# {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
# 10

grade = {'pey': 10, 'julliet': 99}
print(grade['julliet'])
# 99

a = {1: 'a', 2: 'b'}
print(a[1])
# a
print(a[2])
# b

a = {'a': 1, 'b': 2}
print(a['a'])
# 1
print(a['b'])
# 2

dic = {'name': 'pey', 'phone': '0119993323', 'birth':'1118'}
print(dic['name'])
# pey
print(dic['phone'])
# 0119993323
print(dic['birth'])
# 1118

a = {1:'a', 1:'b'}
print(a)
# {1: 'b'}

a = {1:'a', 2:[1, 2, 3]}
print(a[2])
# [1, 2, 3]