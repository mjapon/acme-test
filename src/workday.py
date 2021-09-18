from schedule import EmployeeSchedule
from ctes import schedule_types, schedule_types_info
from utils import compute_payment


class WorkDay:

    def __init__(self, day, start_time, end_time):
        self.day = day
        self.emp_schedule = EmployeeSchedule(start_time, end_time)

    def compute_payment(self):
        entry = self.emp_schedule.entry
        departure = self.emp_schedule.departure

        if entry.type == departure.type:
            return compute_payment(entry.time, departure.time, entry.get_hour_cost(self.day))
        else:
            payment = compute_payment(entry.time, entry.acme_schedule.max_time,
                                      entry.get_hour_cost(self.day))
            entry_time_idx = schedule_types.index(entry.type)

            for it_type in schedule_types[entry_time_idx + 1:]:
                if it_type == departure.type:
                    return payment + compute_payment(departure.acme_schedule.min_time, departure.time,
                                                     departure.get_hour_cost(self.day))
                else:
                    sch_type_info = schedule_types_info[it_type]
                    payment = payment + compute_payment(sch_type_info.min_time, sch_type_info.max_time,
                                                        sch_type_info.get_hour_cost(self.day))
