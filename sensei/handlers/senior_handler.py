from sensei.emp_types import Senior
from programmer.handlers.handler import Handler
from sensei.utils import Rank


class SeniorHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == Rank.SENIOR:
            employee = Senior(**data)

            company.attach(employee)

            return employee
        return False
