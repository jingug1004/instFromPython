a = "20010331Rainy"
date = a[:4]
weather = a[8:]

print(date)
print(weather)
# 2001
# Rainy



year = a[:4]
day = a[4:8]
weather = a[8:]

print(year)
print(day)
print(weather)
# 2001
# Rainy
# 2001
# 0331
# Rainy



b = "Pithon"
print(b[:1] + "y" + b[2:])
# 2001
# Rainy
# 2001
# 0331
# Rainy
# Python



c = "I eat %d apples." % 3
print(c)

d = "I eat %s apples." % "three"
print(d)

number = 3
e = "I eat %d apples." %number
print(e)

number = 10
day = "three"
f = "I eat %d apples. so I was sick for %s days." % (number, day)
print(f)
# 2001
# Rainy
# 2001
# 0331
# Rainy
# Python
# I eat 3 apples.
# I eat three apples.
# I eat 3 apples.
# I eat 10 apples. so I was sick for three days.



format01 = "I hav %s apples" % 3
print(format01)
format02 = "rate is %s" % 3.234
print(format02)
# 2001
# Rainy
# 2001
# 0331
# Rainy
# Python
# I eat 3 apples.
# I eat three apples.
# I eat 3 apples.
# I eat 10 apples. so I was sick for three days.
#     I hav 3 apples
# rate is 3.234



g = "Error is %d%%." % 98
print(g)
# 2001
# Rainy
# 2001
# 0331
# Rainy
# Python
# I eat 3 apples.
# I eat three apples.
# I eat 3 apples.
# I eat 10 apples. so I was sick for three days.
#     I hav 3 apples
# rate is 3.234
# Error is 98%.



h = "% 10s" % "hi"
print(h)

i = "% -10sjane." % "hi"
print(i)
# 2001
# Rainy
# 2001
# 0331
# Rainy
# Python
# I eat 3 apples.
# I eat three apples.
# I eat 3 apples.
# I eat 10 apples. so I was sick for three days.
#     I hav 3 apples
# rate is 3.234
# Error is 98%.
#         hi
# hi        jane.



j = "%0.4f" %3.42134234
print(j)

k = "%10.4f" %3.42134234
# print(k)
# 2001
# Rainy
# 2001
# 0331
# Rainy
# Python
# I eat 3 apples.
# I eat three apples.
# I eat 3 apples.
# I eat 10 apples. so I was sick for three days.
#     I hav 3 apples
# rate is 3.234
# Error is 98%.
#        hi
# hi        jane.
# 3.4213
#     3.4213
