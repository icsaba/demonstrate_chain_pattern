from sensei.utils import Rank


class Employee(object):

    def __init__(self, name, title, age):
        self.name = name
        self.title = title
        self.age = age
        self.salary = None
        self.car = None
        self.compensation_package = None
        self.associates = []

    def is_minion(self):
        return self.title == Rank.MINION

    def is_junior(self):
        return self.title == Rank.JUNIOR

    def is_senior(self):
        return self.title == Rank.SENIOR

    def is_ceo(self):
        return self.title == Rank.CEO