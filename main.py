from datetime import date

from application.salary import calculate_salary
from application.db.people import get_employees

print(f'Today is {date.today()}.')
calculate_salary()
get_employees()