import sys

from workday import WorkDay
from utils import valid_input


def get_payment_by_day(time_interval):
    day = time_interval[0:2]
    interval = time_interval[2:].split('-')
    workday = WorkDay(day, interval[0], interval[1])
    return workday.compute_payment()


def compute_total_payment(days_array):
    total_payment = 0
    for day in days_array:
        total_payment = total_payment + get_payment_by_day(day)
    return int(total_payment)


def compute_payment(input_data):
    employee = input_data.split('=')[0]
    diaslist = input_data.split('=')[1].split(',')
    payment = compute_total_payment(diaslist)
    output_str = 'The amount to pay {} is: {} USD'.format(employee, str(payment))
    return output_str


if __name__ == '__main__':
    print('Acme Test Manuel Japon:')
    try:
        input = sys.argv[1]
        valid_input(input)
        print(compute_payment(input))
    except Exception as error:
        print('Error:', error)
