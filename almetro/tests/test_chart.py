"""
Metro test.

"""
import time
from unittest.mock import patch, MagicMock, call
from matplotlib import pyplot as plt
from hamcrest import (
    assert_that,
    equal_to,
    has_entries,
    has_items,
    close_to
)
from almetro.chart import Chart, ChartAxis
from almetro.complexity import cn_quadratic

def test_should_setup_axis():
    data = {0.: 0., 1.: 3., 2.: 4., 3.: 5.}
    title = 'Ratio'
    label = 'c'
    color = 'tab:green'
    axis = ChartAxis(data, title, label, color)
    plt.close()
    ax1 = plt.subplot()
    
    axis.setup(ax1)

    rt_x, rt_y = axis.line.get_xydata().T    
    assert_that(rt_x, has_items(*list(data.keys())))
    assert_that(rt_y, has_items(*list(data.values())))
    assert_that(axis.line.get_label(), equal_to('c'))
    assert_that(ax1.get_title(), equal_to('Ratio'))

@patch('almetro.chart.ChartAxis.new')
def test_should_show_chart(chartaxis_factory_mock):  
    caxis1, caxis2, caxis3 = MagicMock(), MagicMock(), MagicMock()
    chartaxis_factory_mock.side_effect = [caxis1, caxis2, caxis3]
    experimental=MagicMock()
    ratio=MagicMock()
    theoretical=MagicMock()
    complexity_text = 'complexity text'
    complexity=MagicMock()
    complexity.text.return_value = complexity_text
    elapsed_time=MagicMock()      
    chart = Chart(
                experimental=experimental,
                ratio=ratio,
                theoretical=theoretical,
                complexity=complexity,
                elapsed_time=elapsed_time
            )
    
    chart.show()

    assert_that(chart.ratio, equal_to(caxis1))
    assert_that(chart.experimental, equal_to(caxis2))
    assert_that(chart.theoretical, equal_to(caxis3))

    chartaxis_factory_mock.has_calls([
        call(ratio, 'Ratio', 'c', 'tab:green'),
        call(experimental, 'Experimental', '$\mathcal{T}(\mathcal{f}(n))$', 'tab:blue'),
        call(theoretical, 'Theoretical', complexity_text, 'tab:red')
    ])