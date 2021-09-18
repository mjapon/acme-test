from utils import format_time


class AcmeSchedule:
    def __init__(self, min, max, cost, spcost):
        self.min = min
        self.max = max
        self.cost = cost
        self.special_cost = spcost

        self.min_time = format_time(self.min)
        self.max_time = format_time(self.max)

    def get_hour_cost(self, day):
        if day in ['SA', 'SU']:
            return self.special_cost
        else:
            return self.cost
