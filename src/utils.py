from datetime import datetime
import re

re_name = '[A-Za-z]+'
re_day = '(MO|TU|WE|TH|FR|SA|SU)'
re_time = '(([0-1][0-9]|2[0-3]):[0-5][0-9])'
re_working_time = '{}-{}'.format(re_time, re_time)
re_day_working_time = '{}{}'.format(re_day, re_working_time)
re_input_line = '^{}={}(,{})*$'.format(re_name, re_day_working_time, re_day_working_time)


def valid_input(str_input):
    if re.match(re_input_line, str_input):
        matchobj = re.finditer(re_working_time, str_input)
        for item in matchobj:
            if not item.group(1) < item.group(3):
                raise ValueError('The entry time ({}) could not be greater than the departure time ({})'.format(
                    item.group(1), item.group(3)))
    else:
        raise Exception('Incorrect Value')


def format_time(time_str):
    t_format = '%H:%M'
    zero_time = datetime.strptime('00:00', t_format)
    output = datetime.strptime(time_str, t_format) - zero_time
    return output


def compute_payment(start, end, hour_cost):
    worked_time = end - start
    worked_time_hours = worked_time.seconds / 3600.0
    return int(worked_time_hours * hour_cost)
