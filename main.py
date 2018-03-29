import experienced_intern.company
import kindergarden.company
import intern.company
import programmer.company
import sensei.company
from sensei.utils import Rank

if __name__ == '__main__':
    # c = kindergarden.company.Company()
    # c = intern.company.Company()
    # c = experienced_intern.company.Company()
    # c = programmer.company.Company()
    c = sensei.company.Company()

    employees = [
        {
            'name': 'Csaba I.',
            'age': 25,
            'title': Rank.CEO
        },
        {
            'name': 'Some One 1',
            'age': 30,
            'title': Rank.SENIOR
        },
        {
            'name': 'Some One 2',
            'age': 30,
            'title': Rank.JUNIOR
        },
        {
            'name': 'Some One 3',
            'age': 18,
            'title': Rank.MINION
        },
        {
            'name': 'Some One 4',
            'age': 19,
            'title': Rank.MINION
        }
    ]

    for emp in employees:
        c.add_new_employee(emp)

    for emp in c.employees:
        print vars(emp)
