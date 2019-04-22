"""
Metro test.

"""
from hamcrest import (
    assert_that,
    equal_to,
    has_entry,
    all_of,
    has_items
)
from almetro import Metro

def assert_plot_line(line, x, y):    
    x_plot, y_plot = line.get_xydata().T
    print(line, x, x_plot, y, y_plot)
    assert_that(x_plot, has_items(*x))
    assert_that(y_plot, has_items(*y))    

def test_register_min_time():
    metro = Metro()
    metro.register((1, 2, 3, 4, 5, 6,), [45, 88, 17])
    assert_that(metro.stats(), has_entry(6 , 17))
    assert_that(metro.reference_stats(), has_entry(6 , 6))


def test_registerall_min_times():
    metro = Metro()
    metro.register((1, 2, 3, 4,), [0, 1, 2])
    metro.register((1, 2, 3, 4, 5,), [1, 2, 3])
    assert_that(metro.stats(), all_of(has_entry(4, 0), has_entry(5, 1)))  
    assert_that(metro.reference_stats(), all_of(has_entry(4, 4), has_entry(5, 5)))          

def test_plot():
    metro = Metro()
    metro.register([1], [2])
    metro.register([1, 2], [4])
    line2, line1 = metro.plot()
    assert_plot_line(line1, [1,2], [2.,4.])
    assert_plot_line(line2, [1,2], [1., 2.])
