import pytest
from main import compute_payment, get_payment_by_day


@pytest.mark.parametrize(
    "input, expected",
    [
        ('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
         'The amount to pay RENE is: 215 USD'),
        ('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'The amount to pay ASTRID is: 85 USD')
    ]

)
def test_payment_expected(input, expected):
    balance = compute_payment(input)
    assert balance == expected


@pytest.mark.parametrize(
    "worked_day, expected",
    [
        ('MO10:00-12:00', 30),
        ('TH12:00-14:00', 30)
    ]

)
def test_payment_expected_by_day(worked_day, expected):
    day_payment = get_payment_by_day(worked_day)
    assert day_payment == expected
