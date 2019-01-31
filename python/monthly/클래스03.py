'''
어떤 회사가 직원들의 연봉을 매년 1회 인상해 주는데
특이하게도 전직원의 연봉을 똑같은 인상률로 인상해줌
'''


class Employee:

    def __init__(self, name, lastname, money):
        self.name = name
        self.lastname = lastname
        self.money = money

    def up_money(self):
        self.money = self.money * 1.1
        return int(self.money)


emp_1 = Employee('Sanghee', 'Lee', 50000)
emp_2 = Employee('Minjung', 'Kim', 60000)


print(emp_1.up_money())
print(emp_2.up_money())