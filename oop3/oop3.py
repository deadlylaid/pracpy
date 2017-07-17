class Employee(object):
    '''
    직원 관리 클래스
    '''

    raise_amount = 1.1
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

        Employee.num_of_emps += 1

    def __del__(self):
        Employee.num_of_emps -= 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * 1.1)
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)
emp_1 = Employee('minsoo', 'han', 5000)
emp_2 = Employee('jisoo', 'han', 4000)
print(Employee.num_of_emps)

del emp_1
del emp_2
print(Employee.num_of_emps)
