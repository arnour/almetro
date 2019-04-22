"""
Plot test.

"""
from hamcrest import (
    assert_that,
    equal_to,
    has_entry,
    all_of,
    has_items
)
from unittest.mock import MagicMock
from almetro import Metro, Plot
from almetro.complexity import n_quadratic

def assert_plot_line(line, x, y, label):    
    x_plot, y_plot = line.get_xydata().T
    print(line, x, x_plot, y, y_plot)
    assert_that(x_plot, has_items(*x))
    assert_that(y_plot, has_items(*y))
    assert_that(line.get_label(), equal_to(label))

def test_plot():
    metro = MagicMock()
    metro.stats.return_value = {0: 0, 1: 1, 2: 2}
    metro.reference_stats.return_value = {0: 0, 1: 1, 2: 4}
    metro.complexity.return_value = n_quadratic
    
    plot = Plot(metro)
    
    plot.show()

    assert_plot_line(plot.theoretical_line, [0, 1, 2], [0., 1.,4.], n_quadratic.text())
    assert_plot_line(plot.algorithm_line, [0, 1, 2], [0., 1., 2.], 'Your algorithm')    