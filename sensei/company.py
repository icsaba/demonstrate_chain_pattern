from sensei.factory.handler_factory import HandlerFactory
from sensei.handlers.ceo_handler import CEOHandler
from sensei.handlers.default_handler import DefaultHandler
from sensei.handlers.junior_handler import JuniorHandler
from sensei.handlers.senior_handler import SeniorHandler
from sensei.observer.subject import Subject


class Company(Subject):

    def __init__(self):
        super(Company, self).__init__()

        self.employees = []
        self.base_salary = 2

        self.handler = HandlerFactory.generate([
            CEOHandler,
            SeniorHandler,
            JuniorHandler,
            DefaultHandler
        ])

    def calculate_ceo_salary(self):
        return self.base_salary * 5 * max([len(self.employees)-1, 1])

    def calculate_senior_salary(self):
        return self.calculate_ceo_salary() * 0.8

    def calculate_junior_salary(self):
        return self.base_salary * 3

    def add_new_employee(self, data):
        """
        :param data: { 'name': str, 'age': int, 'title': str }
        :return:
        """

        employee = self.handler.handle(data, self)
        self.employees.append(employee)
        self.notify()
