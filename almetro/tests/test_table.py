"""
Metro table test.

"""
from almetro import table
from almetro.metro import Metro
from almetro.complexity import Complexity
from almetro.tests import TestBase, matchers as m, mock


class TestTable(TestBase):

    @mock.patch('almetro.complexity.Complexity.text', new_callable=mock.PropertyMock, return_value='cn')    
    @mock.patch('almetro.metro.Metro.ratio', new_callable=mock.PropertyMock, return_value={1: 1, 2: 0.5, 3: 0.33})
    @mock.patch('almetro.metro.Metro.theoretical', new_callable=mock.PropertyMock, return_value={1: 1, 2: 4, 3: 9})    
    @mock.patch('almetro.metro.Metro.experimental', new_callable=mock.PropertyMock, return_value={1: 1, 2: 2, 3: 3})
    @mock.patch('tabulate.tabulate')
    def test_should_create_tabulated_data(self, tabulate_mock, *mocks):

        table.build_table(Metro(Complexity()))

        tabulate_mock.assert_called_once_with(
            [
                (1, 1, 1, 1),
                (2, 2, 4, 0.5),
                (3, 3, 9, 0.33)
            ],
            headers=['n', 'experimental', 'theoretical cn', 'ratio'],
            tablefmt='fancy_grid'
        )
