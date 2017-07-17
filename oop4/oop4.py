class Employee:

    raise_amount = 1.1

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolweb.net'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def get_pay(self):
        return '현재 "{}"의 연봉은 "{}"입니다'.format(self.full_name, self.pay)

    @classmethod
    def change_raise_amount(cls, amount):
        while amount < 1:
            print('[경고] 인상율이 "1"보다 작을 수 없습니다')
            amount = input('[입력] 인상율을 다시 입력하여 주십시오. \n=>')
            amount = float(amount)
        cls.raise_amount = amount
        print('인상율 "{}"가 적용 되었습니다.'.format(amount))

emp_1 = Employee('minsoo', 'han', 500000)
emp_2 = Employee('jisoo', 'han', 400000)

print(emp_1.get_pay())
print(emp_2.get_pay())

Employee.change_raise_amount(0.9)

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.get_pay())
print(emp_2.get_pay())
