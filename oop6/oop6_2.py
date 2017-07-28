class MyInt(int):
    def __add__(self, other):
        return '{} 더하기 {}는 {} 입니다.'.format(self.real, other.real, self.real + other.real)

my_num = MyInt(5)

print(my_num + 5)

#print(type(my_num))
#
#print(isinstance(my_num, int))
#
#print(MyInt.__bases__)
#
#print(my_num + 5)
#
#print(dir(my_num))
#
#print(my_num.__add__(5))
