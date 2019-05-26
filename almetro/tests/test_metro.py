"""
Metro test.

"""
import time
from almetro.tests import TestBase, mock, matchers as m
from almetro.metro import Metro
from almetro.complexity import cn


class TestMetro(TestBase):

    def test_register_min_time_for_each_call(self):
        metro = Metro(cn)
        time.sleep(0.1)
        metro.register(6, [45, 88, 17])
        time.sleep(0.1)
        metro.register(7, [45, 88, 37, 22])
        m.assert_that(metro.experimental, m.has_entries({6: 17, 7: 22}))
        m.assert_that(metro.elapsed_time, m.close_to(0.2, 0.05))
        m.assert_that(metro.processed, m.equal_to(False))

    def test_should_process_experimental_data_for_metro(self):
        metro = Metro(cn)

        metro.register(1, [1, 2, 3])
        metro.register(2, [2, 3, 4])
        metro.register(3, [3, 4, 5])

        metro.process()

        m.assert_that(metro.processed, m.equal_to(True))
        m.assert_that(metro.elapsed_time, m.is_not(m.equal_to(0)))
        m.assert_that(metro.theoretical, m.equal_to({1: 1, 2: 2, 3: 3}))
        m.assert_that(metro.ratio, m.equal_to({1: 1.0, 2: 1.0, 3: 1.0}))

    def test_should_raise_error_if_theo_complexity_is_not_given(self):

        metro = Metro(None)

        m.assert_that(m.calling(metro.process), m.raises(ValueError))

    @mock.patch('almetro.metro.Metro.process')
    @mock.patch('almetro.chart.build_chart')
    def test_should_create_chart_for_metro(self, build_chart_mock, metro_process_mock):
        metro = Metro(cn)
        metro.chart()
        build_chart_mock.assert_called_once_with(metro)
        metro_process_mock.assert_called_once()

    @mock.patch('almetro.metro.Metro.process')
    @mock.patch('almetro.table.build_table')
    def test_should_create_table_for_metro(self, build_table_mock, metro_process_mock):
        metro = Metro(cn)
        metro.table()
        build_table_mock.assert_called_once_with(metro)
        metro_process_mock.assert_called_once()
