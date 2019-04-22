"""
Complexity test.

"""
from hamcrest import (
    assert_that,
    instance_of,
    has_length,
    has_items,
    matches_regexp,
    is_not,
    equal_to,
)
import almetro.complexity as complexity


def test_should_return_n():
    assert_that(complexity.n.fn()(1), equal_to(1))
    assert_that(complexity.n.fn()(10), equal_to(10))

def test_should_return_n_quadratic():
    assert_that(complexity.n_quadratic.fn()(1), equal_to(1))
    assert_that(complexity.n_quadratic.fn()(3), equal_to(9))
    assert_that(complexity.n_quadratic.fn()(10), equal_to(100))

def test_should_return_n_cubic():
    assert_that(complexity.n_cubic.fn()(1), equal_to(1))
    assert_that(complexity.n_cubic.fn()(3), equal_to(27))
    assert_that(complexity.n_cubic.fn()(10), equal_to(1000))

def test_should_return_n_log_n():
    assert_that(complexity.n_log_n.fn()(8), equal_to(24))
    assert_that(complexity.n_log_n.fn()(32), equal_to(160))

def test_should_return_log_n():
    assert_that(complexity.log_n.fn()(8), equal_to(3))
    assert_that(complexity.log_n.fn()(32), equal_to(5))