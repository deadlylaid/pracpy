import student


class Employee(object):

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('minsoo', 'Han', 0)
emp_2 = Employee('jisoo', 'Han', 1)

print(emp_1.email)
print(emp_2.email)

print(emp_1.full_name)

print(student.name)
