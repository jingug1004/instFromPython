def GuGu(n):
    result = []
    result.append(n * 1)
    result.append(n * 2)
    result.append(n * 3)
    result.append(n * 4)
    result.append(n * 5)
    result.append(n * 6)
    result.append(n * 7)
    result.append(n * 8)
    result.append(n * 9)
    return result


print(GuGu(2))


# [2, 4, 6, 8, 10, 12, 14, 16, 18]

def GuGU02(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result


print(GuGU02(2))
# [2, 4, 6, 8, 10, 12, 14, 16, 18]



# nnn = 1
# while nnn < 1000:
#     print(nnn)
#     nnn += 1
#
# for n in range(1, 1000):
#     print(n)

for n in range(1, 20):
    if n % 3 == 0 or n % 5 == 0:
        print(n)
