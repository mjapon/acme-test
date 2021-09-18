from ctes import schedule_types, schedule_types_info
from utils import format_time


class EmployeeSchedule:

    def __init__(self, start, end):
        self.entry = WorkingHour(start)
        self.departure = WorkingHour(end)


class WorkingHour:

    def __init__(self, time_str):
        self.time = format_time(time_str)
        self.acme_schedule, self.type = self.get_acme_schedule_info(time_str)

    @staticmethod
    def get_acme_schedule_info(time_str):
        for schedule in schedule_types:
            schedule_info = schedule_types_info[schedule]
            if schedule_info.min <= time_str <= schedule_info.max:
                return schedule_info, schedule

    def get_hour_cost(self, day):
        return self.acme_schedule.get_hour_cost(day)
