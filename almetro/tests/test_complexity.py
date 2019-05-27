"""
Complexity test.

"""
from almetro.tests import TestBase, matchers as m
from almetro.complexity import cn, cn_quadratic, cn_cubic, clog_n, cn_log_n, c_one


class TestComplexity(TestBase):

    def test_should_return_n(self):
        m.assert_that(cn.theoretical(1), m.equal_to(1))
        m.assert_that(cn.theoretical(10), m.equal_to(10))
        m.assert_that(cn.experimental(1), m.equal_to(1))
        m.assert_that(cn.experimental(10), m.equal_to(10))

    def test_should_return_n_quadratic(self):
        m.assert_that(cn_quadratic.theoretical(1), m.equal_to(1))
        m.assert_that(cn_quadratic.theoretical(3), m.equal_to(9))
        m.assert_that(cn_quadratic.theoretical(10), m.equal_to(100))

        m.assert_that(cn_quadratic.experimental(1), m.equal_to(1))
        m.assert_that(cn_quadratic.experimental(3), m.equal_to(3))
        m.assert_that(cn_quadratic.experimental(10), m.equal_to(10))

    def test_should_return_n_cubic(self):
        m.assert_that(cn_cubic.theoretical(1), m.equal_to(1))
        m.assert_that(cn_cubic.theoretical(3), m.equal_to(27))
        m.assert_that(cn_cubic.theoretical(10), m.equal_to(1000))

        m.assert_that(cn_cubic.experimental(1), m.equal_to(1))
        m.assert_that(cn_cubic.experimental(3), m.equal_to(3))
        m.assert_that(cn_cubic.experimental(10), m.equal_to(10))

    def test_should_return_n_log_n(self):
        m.assert_that(cn_log_n.theoretical(8), m.equal_to(24))
        m.assert_that(cn_log_n.theoretical(32), m.equal_to(160))

        m.assert_that(cn_log_n.experimental(8), m.equal_to(8))
        m.assert_that(cn_log_n.experimental(32), m.equal_to(32))

    def test_should_return_log_n(self):
        m.assert_that(clog_n.theoretical(8), m.equal_to(3))
        m.assert_that(clog_n.theoretical(32), m.equal_to(5))

        m.assert_that(clog_n.experimental(8), m.equal_to(8))
        m.assert_that(clog_n.experimental(32), m.equal_to(32))

    def test_should_return_c(self):
        m.assert_that(c_one.theoretical(8), m.equal_to(1))
        m.assert_that(c_one.theoretical(32), m.equal_to(1))

        m.assert_that(c_one.experimental(8), m.equal_to(8))
        m.assert_that(c_one.experimental(32), m.equal_to(32))
