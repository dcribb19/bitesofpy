import pytest

from workouts import print_workout_days

@pytest.mark.parametrize('check, expected', [
    ('1', 'Mon, Tue\n'),
    ('2', 'Thu, Fri\n'),
    ('up', 'Mon, Thu\n'),
    ('UP', 'Mon, Thu\n'),
    ('low', 'Tue, Fri\n'),
    ('Low', 'Tue, Fri\n'),
    ('body', 'Mon, Tue, Thu, Fri\n'),
    ('#', 'Mon, Tue, Thu, Fri\n'),
    ('mIn', 'Wed\n'),
    ('zero', 'No matching workout\n')
])


def test_print_workout_days(capsys, check, expected):
    print_workout_days(check)
    captured = capsys.readouterr()
    assert captured.out == expected
