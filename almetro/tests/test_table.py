"""
Metro table test.

"""
from almetro import table
from almetro.metro import Metro
from almetro.complexity import Complexity
from almetro.tests import TestBase, mock
from almetro.instance import Instance

instance = Instance(name='instance', value={}, size={'n': 'n'})


class TestTable(TestBase):

    @mock.patch('almetro.complexity.Complexity.text', new_callable=mock.PropertyMock, return_value='cn')
    @mock.patch('almetro.metro.Metro.instances', new_callable=mock.PropertyMock, return_value={1: instance, 2: instance, 3: instance})
    @mock.patch('almetro.metro.Metro.ratio', new_callable=mock.PropertyMock, return_value={1: 1, 2: 0.5, 3: 0.33})
    @mock.patch('almetro.metro.Metro.theoretical', new_callable=mock.PropertyMock, return_value={1: 1, 2: 4, 3: 9})
    @mock.patch('almetro.metro.Metro.experimental', new_callable=mock.PropertyMock, return_value={1: 1, 2: 2, 3: 3})
    @mock.patch('tabulate.tabulate')
    def test_should_create_tabulated_data(self, tabulate_mock, *mocks):

        table.build_table(Metro(Complexity()))

        tabulate_mock.assert_called_once_with(
            [
                ('instance n=n', 1, 1, 1),
                ('instance n=n', 2, 4, 0.5),
                ('instance n=n', 3, 9, 0.33)
            ],
            headers=['size', 'experimental', 'theoretical cn', 'ratio'],
            tablefmt='fancy_grid'
        )

    @mock.patch('almetro.table.tprint', autospec=True)
    def test_show_table(self, mock_print):
        table_instance = table.Table('data')
        table_instance.show()
        mock_print.assert_called_with('data')
