"""
Complexity test.

"""
from hamcrest import (
    assert_that,
    equal_to,
)
from almetro.complexity import cn, cn_quadratic, cn_cubic, clog_n, cn_log_n, c_one


def test_should_return_n():
    assert_that(cn.fn()(1), equal_to(1))
    assert_that(cn.fn()(10), equal_to(10))


def test_should_return_n_quadratic():
    assert_that(cn_quadratic.fn()(1), equal_to(1))
    assert_that(cn_quadratic.fn()(3), equal_to(9))
    assert_that(cn_quadratic.fn()(10), equal_to(100))


def test_should_return_n_cubic():
    assert_that(cn_cubic.fn()(1), equal_to(1))
    assert_that(cn_cubic.fn()(3), equal_to(27))
    assert_that(cn_cubic.fn()(10), equal_to(1000))


def test_should_return_n_log_n():
    assert_that(cn_log_n.fn()(8), equal_to(24))
    assert_that(cn_log_n.fn()(32), equal_to(160))


def test_should_return_log_n():
    assert_that(clog_n.fn()(8), equal_to(3))
    assert_that(clog_n.fn()(32), equal_to(5))


def test_should_return_c():
    assert_that(c_one.fn()(8), equal_to(1))
    assert_that(c_one.fn()(32), equal_to(1))
