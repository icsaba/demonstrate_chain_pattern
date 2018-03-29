from employee import Employee
from sensei.observer.observer import Observer


class CEO(Employee, Observer):

    def __init__(self, name, title, age):
        super(CEO, self).__init__(name, title, age)

        self.compensation_package = ['free money', 'cafeteria', '+1 free day']
        self.car = 'Rolls Royce' if age > 50 else 'Bentley Coupe'

    def update(self, company):
        self.associates = [emp.name for emp in company.employees if emp.is_senior()]
        self.salary = company.calculate_ceo_salary()


class Senior(Employee, Observer):

    def __init__(self, name, title, age):
        super(Senior, self).__init__(name, title, age)

        self.compensation_package = ['cafeteria', '+1 free day']

    def update(self, company):
        self.salary = company.calculate_senior_salary()
        self.car = 'VW Passat' if self.salary > 20 else 'VW Jetta'
        self.associates = [emp.name for emp in company.employees if emp.is_junior()]


class Junior(Employee, Observer):

    def __init__(self, name, title, age):
        super(Junior, self).__init__(name, title, age)

        self.compensation_package = ['+1 free day']
        self.car = 'VW Jetta'

    def update(self, company):
        self.salary = company.calculate_junior_salary()
        self.associates = [emp.name for emp in company.employees if emp.is_minion()]
