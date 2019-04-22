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
from almetro.complexity import n as complexity_n, n_quadratic

 
def test_register_min_time():
    metro = Metro(complexity_n)
    metro.register((1, 2, 3, 4, 5, 6,), [45, 88, 17])
    assert_that(metro.stats(), has_entry(6 , 17))
    assert_that(metro.reference_stats(), has_entry(6 , 6))


def test_registerall_min_times():
    metro = Metro(complexity_n)
    metro.register((1, 2, 3, 4,), [0, 1, 2])
    metro.register((1, 2, 3, 4, 5,), [1, 2, 3])
    assert_that(metro.stats(), all_of(has_entry(4, 0), has_entry(5, 1)))  
    assert_that(metro.reference_stats(), all_of(has_entry(4, 4), has_entry(5, 5)))

def test_registerall_min_times_and_calculate_theoretical_complexity():
    metro = Metro(n_quadratic)
    metro.register((1, 2, 3, 4,), [0, 1, 2])
    metro.register((1, 2, 3, 4, 5,), [1, 2, 3])
    assert_that(metro.stats(), all_of(has_entry(4, 0), has_entry(5, 1)))  
    assert_that(metro.reference_stats(), all_of(has_entry(4, 16), has_entry(5, 25)))    