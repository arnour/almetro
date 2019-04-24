"""
Metro test.

"""
from unittest.mock import MagicMock
from matplotlib import pyplot as plt
from hamcrest import (
    assert_that,
    equal_to,
    has_items,
)
from almetro.chart import Chart, ChartAxis, ChartLine


def get_axis():
    plt.close()
    return plt.subplots(1, 2, sharex=True)


def test_should_setup_line():
    _, axes = get_axis()
    axis = axes[0]

    data = {0.: 0., 1.: 3., 2.: 4., 3.: 5.}
    label = 'c'
    line = ChartLine(data, label, 'tab:green')
    line.setup(axis)

    rt_x, rt_y = line.plt_line.get_xydata().T
    assert_that(rt_x, has_items(*list(data.keys())))
    assert_that(rt_y, has_items(*list(data.values())))
    assert_that(line.plt_line.get_label(), equal_to(label))


def test_should_setup_axis():
    _, axes = get_axis()
    axis = axes[0]

    title = 'Ratio'
    chart_lines = [MagicMock()]
    chart_axis = ChartAxis(title, chart_lines)

    chart_axis.setup(axis)

    assert_that(chart_axis.plt_axis.get_title(), equal_to(title))
    chart_lines[0].setup.assert_called_once_with(axis)


def test_should_show_chart():
    title = 'Experimental'
    chart_axes = [MagicMock(), MagicMock()]

    chart = Chart(title, chart_axes)

    chart.show()

    chart_axes[0].setup.assert_called_once()
