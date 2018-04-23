class FourCal:
    pass


a = FourCal()


# print(type(a))
# <class '__main__.FourCal'>

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result


a = FourCal()
a.setdata(4, 2)
print(a.sum())
# 6

class HousePark01:
    lastname = "박"

    def setname(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s여행을 가다. " % (self.fullname, where))


pey = HousePark01()
pes = HousePark01()
print(pey.lastname)
# 박
print(pes.lastname)
# 박

pey = HousePark01()
pey.setname("응용")
print(pey.fullname)
# 박응용

# temp = pey.travel("부산")
print(pey.travel("부산"))
# 박응용, 부산여행을 가다.

class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s여행을 가다. " % (self.fullname, where))

pey = HousePark("동열")
print(pey.travel("태국"))
# 박동열, 태국여행을 가다.

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가다. " % (self.fullname, where, day))


juliet = HouseKim("줄리엣")    
print(juliet.travel("독도", 3))
# 김줄리엣, 독도여행 3일 가다.

class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s 여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))

pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.love(juliet)
a = pey + juliet
print(a)
# 박응용, 김줄리엣 사랑에 빠졌네
# 박응용, 김줄리엣 결혼했네









