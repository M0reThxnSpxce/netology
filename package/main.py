from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

def main():
    pass

if __name__ == '__main__':

    current_date = datetime.now().date()

    print("Текущая дата: %d день недели, %d/%d/%d." % (current_date.weekday()+1, current_date.day, current_date.month, current_date.year))
    calculate_salary()
    get_employees()