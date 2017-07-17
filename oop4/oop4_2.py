class Person:

    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return '{}년 {}월{}일생 {}입니다'.format(self.year, self.month, self.day, self.sex)

    @classmethod
    def ssn_person(cls,ssn):
        front, back = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[:2]
        else:
            year = '20' + front[:2]

        if(int(sex) % 2) == 0:
            sex = '여성'
        else:
            sex = '남성'

        month = front[2:4]
        day = front[4:6]

        return cls(year, month, day, sex)

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

person_1 = Person.ssn_person('921399-1169999')
print(person_1)

person_2 = Person.ssn_person('051399-4169999')
print(person_2)

import datetime

my_date = datetime.date(2017, 7, 16)

#클래스를 통해 스테틱 메소드 호출
print(Person.is_work_day(my_date))
#인스턴스를 통해 호출
print(person_1.is_work_day(my_date))
