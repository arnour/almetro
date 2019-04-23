"""
Algorithms test.
"""
from hamcrest import (
    assert_that,
    equal_to,
)
from almetro.algorithms import loop_n, loop_n_quadratic, loop_n_cubic, loop_n_log, loop_n_log_n

def test_should_execute_n_times():    
    assert_that(loop_n(list(range(5))), equal_to(5))

def test_should_execute_n_quadratic_times():    
    assert_that(loop_n_quadratic(list(range(5))), equal_to(25))

def test_should_execute_n_cubic_times():    
    assert_that(loop_n_cubic(list(range(5))), equal_to(125))

def test_should_execute_log_n_times():    
    assert_that(loop_n_log(list(range(8))), equal_to(3))

def test_should_execute_n_log_n_times():    
    assert_that(loop_n_log_n(list(range(8))), equal_to(24))    