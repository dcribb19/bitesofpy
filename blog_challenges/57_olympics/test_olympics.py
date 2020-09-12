import pytest
from olympics import most_medals_by_athlete


@pytest.mark.parametrize('n, expected', [
    ('Men', 'Michael Phelps'),
    ('Women', 'Larisa Latynina')
])
def test_most_medals_by_athlete(n, expected):
    actual = most_medals_by_athlete(n)
    assert actual == expected
