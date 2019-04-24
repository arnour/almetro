"""
Metro test.

"""
import time
from unittest.mock import patch
from hamcrest import (
    assert_that,
    has_entries,
    close_to
)
from almetro.metro import Metro
from almetro.complexity import cn

 
def test_register_min_time_for_each_call():
    metro = Metro()
    time.sleep(0.1)
    metro.register((1, 2, 3, 4, 5, 6,), [45, 88, 17])
    time.sleep(0.1)
    metro.register((1, 2, 3, 4, 5, 6, 7, ), [45, 88, 37, 22])
    assert_that(metro.experimental, has_entries({6: 17, 7: 22}))
    assert_that(metro.elapsed_time, close_to(0.2, 0.05))

@patch('almetro.chart.build_chart')
def test_should_create_chart_for_metro(build_chart_mock):
    metro = Metro()
    metro.experimental = {0: 0.0, 1: 1.0, 2: 4.0, 3: 9.0}
    metro.chart(cn)
    build_chart_mock.assert_called_once_with(metro, cn)