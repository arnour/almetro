"""
Metro test.

"""
from hamcrest import (
    assert_that,
    equal_to,
    has_items
)
import numpy as np
from almetro import Metro

instance = (1, 2, 3, 4,)


def test_register_min_time():
    metro = Metro()
    metro.register((1, 2, 3, 4, 5, 6,), [45, 88, 17])
    assert_that(metro.stats().tolist(), equal_to([(6, 17.0,)]))


def test_registerall_min_times():
    metro = Metro()
    metro.register((1, 2, 3, 4,), [0, 1, 2])
    metro.register((1, 2, 3, 4, 5,), [1, 2, 3])
    assert_that(metro.stats().tolist(), equal_to([(4, 0.0,), (5, 1.0,)]))

def test_plot():
    metro = Metro()
    metro.register([1], [2])
    metro.register([1, 2], [4])
    line, = metro.plot()
    x_plot, y_plot = line.get_xydata().T
    np.testing.assert_array_equal(x_plot, np.array([1, 2]))
    np.testing.assert_array_equal(y_plot, np.array([2, 4]))
