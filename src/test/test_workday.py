import pytest

from workday import WorkDay


@pytest.mark.parametrize(
    "day, start_time, end_time, expected_payment",
    [
        ('MO', '06:00', '08:00', 50),
        ('SU', '07:00', '08:00', 30),
        ('SA', '07:00', '11:01', 100),
        ('WE', '20:00', '21:00', 20),
        ('MO', '08:00', '10:01', 40),
        ('MO', '08:00', '20:4', 200)
    ]
)
def test_total_payment_by_day(day, start_time, end_time, expected_payment):
    work_day = WorkDay(day, start_time, end_time)
    assert work_day.compute_payment() == expected_payment
