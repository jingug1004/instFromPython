# f = open("C:/Python/새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
#
# f = open("C:/Python/새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다." % i
#     print(data)

# f = open("C:/Python/새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()
# 1번째 줄입니다.
# 2번째 줄입니다.
# 3번째 줄입니다.
# 4번째 줄입니다.
# 5번째 줄입니다.
# 6번째 줄입니다.
# 7번째 줄입니다.
# 8번째 줄입니다.
# 9번째 줄입니다.
# 10번째 줄입니다.

# f = open("C:/Python/새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# while 1:
#     data = input()
#     if not data: break
#     print(data)

# f = open("C:/Python/새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# f = open("C:/Python/새파일.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# f = open("C:/Python/새파일.txt", 'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다!!!!\n" % i
#     f.write(data)
# f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
