import pytest

from schedule import WorkingHour, EmployeeSchedule
from utils import format_time


@pytest.mark.parametrize(
    "time, expected",
    [
        ('07:00', 'a'),
        ('19:00', 'c'),
        ('23:00', 'c'),
        ('04:00', 'a')
    ]
)
def test_schedyle_type_by_time(time, expected):
    shedule = WorkingHour(time)
    assert shedule.type == expected


@pytest.mark.parametrize(
    'time, expected',
    [
        ('06:00', '00:01'),
        ('12:00', '09:01'),
        ('21:00', '18:01'),
        ('01:00', '00:01')

    ]
)
def test_shedule_time_start(time, expected):
    schedule = WorkingHour(time)
    time_expected = format_time(expected)
    assert schedule.acme_schedule.min_time.seconds == time_expected.seconds


@pytest.mark.parametrize(
    'time, expected',
    [
        ('11:00', '18:00'),
        ('14:00', '18:00'),
        ('20:00', '23:59'),
        ('02:00', '09:00')

    ]
)
def test_schedule_time_end(time, expected):
    shedule = WorkingHour(time)
    time_expected = format_time(expected)
    assert shedule.acme_schedule.max_time.seconds == time_expected.seconds


@pytest.mark.parametrize(
    'time_ini, time_end, ini_exp, end_exp',
    [
        ('10:00', '11:00', 'b', 'b'),
        ('12:00', '20:00', 'b', 'c'),
        ('01:00', '08:00', 'a', 'a'),
        ('01:00', '22:00', 'a', 'c')

    ]
)
def test_shedule_type_by_hour(time_ini, time_end, ini_exp, end_exp):
    empschedule = EmployeeSchedule(time_ini, time_end)
    assert empschedule.entry.type == ini_exp
    assert empschedule.departure.type == end_exp
