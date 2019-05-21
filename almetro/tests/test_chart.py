"""
Metro test.

"""
from matplotlib import pyplot as plt
from almetro.tests import TestBase, matchers as m, mock
from almetro.chart import Chart, ChartAxis, ChartLine


def get_axis():
    plt.close()
    return plt.subplots(1, 2, sharex=True)


class TestChart(TestBase):

    def test_should_setup_line(self):
        _, axes = get_axis()
        axis = axes[0]

        data = {0.: 0., 1.: 3., 2.: 4., 3.: 5.}
        label = 'c'
        line = ChartLine(data, label, 'tab:green')
        line.setup(axis)

        rt_x, rt_y = line.plt_line.get_xydata().T
        m.assert_that(rt_x, m.has_items(*list(data.keys())))
        m.assert_that(rt_y, m.has_items(*list(data.values())))
        m.assert_that(line.plt_line.get_label(), m.equal_to(label))

    def test_should_setup_axis(self):
        _, axes = get_axis()
        axis = axes[0]

        title = 'Ratio'
        chart_lines = [mock.MagicMock()]
        chart_axis = ChartAxis(title, chart_lines)

        chart_axis.setup(axis)

        m.assert_that(chart_axis.plt_axis.get_title(), m.equal_to(title))
        chart_lines[0].setup.assert_called_once_with(axis)

    def test_should_show_chart(self):
        title = 'Experimental'
        chart_axes = [mock.MagicMock(), mock.MagicMock()]

        chart = Chart(title, chart_axes)

        chart.show()

        chart_axes[0].setup.assert_called_once()
