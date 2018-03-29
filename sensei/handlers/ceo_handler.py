from sensei.emp_types import CEO
from programmer.handlers.handler import Handler
from sensei.utils import Rank


class CEOHandler(Handler):

    def _handle(self, data, company):

        if data['title'] == Rank.CEO:
            employee = CEO(**data)

            company.attach(employee)

            return employee
        return False
