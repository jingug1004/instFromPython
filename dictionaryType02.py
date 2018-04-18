Key리스트만들기 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(Key리스트만들기.keys())
# dict_keys(['name', 'phone', 'birth'])

for k in Key리스트만들기.keys():
    print(k)
# name
# phone
# birth

aaa = list(Key리스트만들기.keys())
print(aaa)
# ['name', 'phone', 'birth']

Value리스트만들기 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(Value리스트만들기.values())
# dict_values(['pey', '0119993323', '1118'])

KeyValue쌍얻기 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(KeyValue쌍얻기.items())
# dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

KeyValue쌍모두지우기 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(KeyValue쌍모두지우기.clear())
# None

Key로Value얻기 = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(Key로Value얻기.get('name'))
# pey
print(Key로Value얻기.get('phone'))
# 0119993323
print(Key로Value얻기.get('nokey'))
# None

# Key로Value얻기['nokey']
# KeyError: 'nokey'

print(Key로Value얻기.get('foo', 'bar'))
# bar

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print('name' in a)
# True
print('email' in a)
# False