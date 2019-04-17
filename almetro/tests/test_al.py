"""
Al test.

"""
from hamcrest import (
    assert_that,
    has_length,
)
from unittest.mock import MagicMock
from almetro import Metro, Al


def test_should_iterate_5_times_creating_new_instances():
    algorithm = MagicMock()
    instance_provider = MagicMock()
    instance_provider.side_effect = [(0,), (0, 1,), (0, 1, 2,)]
    al = Al(iterations=2, repeat=1, instance_provider=instance_provider)
    metro = al.metro(lambda inst: algorithm(inst))
    assert_that(metro.stats(), has_length(1))
