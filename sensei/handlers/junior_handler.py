from sensei.emp_types import Junior
from programmer.handlers.handler import Handler
from sensei.utils import Rank


class JuniorHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == Rank.JUNIOR:
            employee = Junior(**data)

            company.attach(employee)

            return employee
        return False
