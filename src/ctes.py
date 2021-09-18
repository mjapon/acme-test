from acme import AcmeSchedule


schedule_types = ['a', 'b', 'c']

schedule_types_info = {
    'a': AcmeSchedule('00:01', '09:00', 25, 30),
    'b': AcmeSchedule('09:01', '18:00', 15, 20),
    'c': AcmeSchedule('18:01', '23:59', 20, 25)
}
