"""
Complexity test.

"""
from almetro.tests import TestBase, matchers as m
from almetro.complexity import cn, cn_quadratic, cn_cubic, clog_n, cn_log_n, c_one


class TestComplexity(TestBase):

    def test_should_return_n(self):
        m.assert_that(cn.fn()(1), m.equal_to(1))
        m.assert_that(cn.fn()(10), m.equal_to(10))

    def test_should_return_n_quadratic(self):
        m.assert_that(cn_quadratic.fn()(1), m.equal_to(1))
        m.assert_that(cn_quadratic.fn()(3), m.equal_to(9))
        m.assert_that(cn_quadratic.fn()(10), m.equal_to(100))

    def test_should_return_n_cubic(self):
        m.assert_that(cn_cubic.fn()(1), m.equal_to(1))
        m.assert_that(cn_cubic.fn()(3), m.equal_to(27))
        m.assert_that(cn_cubic.fn()(10), m.equal_to(1000))

    def test_should_return_n_log_n(self):
        m.assert_that(cn_log_n.fn()(8), m.equal_to(24))
        m.assert_that(cn_log_n.fn()(32), m.equal_to(160))

    def test_should_return_log_n(self):
        m.assert_that(clog_n.fn()(8), m.equal_to(3))
        m.assert_that(clog_n.fn()(32), m.equal_to(5))

    def test_should_return_c(self):
        m.assert_that(c_one.fn()(8), m.equal_to(1))
        m.assert_that(c_one.fn()(32), m.equal_to(1))
