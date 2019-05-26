"""
Al test.

"""
from almetro.tests import TestBase, mock, matchers as m
from almetro.al import InstanceSettings, ExecutionSettings, Al
from almetro.instance import growing, generator


class TestAl(TestBase):

    def test_should_create_al_instance_settings_with_default(self):
        instance = InstanceSettings()
        m.assert_that(instance.instances, m.equal_to(1))
        m.assert_that(instance.provider, growing())

    def test_should_create_al_instance_settings(self):
        provider = growing()
        instance = InstanceSettings(instances=5, provider=provider)
        m.assert_that(instance.instances, m.equal_to(5))
        m.assert_that(instance.provider, provider)

    def test_should_create_al_execution_settings_with_default(self):
        execution = ExecutionSettings()
        m.assert_that(execution.trials, m.equal_to(1))
        m.assert_that(execution.runs, m.equal_to(1))

    def test_should_create_al_execution_settings(self):
        execution = ExecutionSettings(trials=5, runs=34)
        m.assert_that(execution.trials, m.equal_to(5))
        m.assert_that(execution.runs, m.equal_to(34))

    @mock.patch('almetro.metro.Metro.new')
    def test_should_measure_algorithm_using_default_setup(self, metro_factory_mock):
        algorithm_mock = mock.MagicMock()
        complexity_mock = mock.MagicMock()
        metro_mock = mock.MagicMock()
        metro_factory_mock.return_value = metro_mock

        metro = Al().metro(algorithm_mock, complexity_mock)

        m.assert_that(metro, m.equal_to(metro_mock))
        algorithm_mock.assert_called_once()
        metro_mock.register.assert_called_once()
        m.assert_that(metro_mock.register.call_args[0][0].name, m.equal_to('growing'))
        m.assert_that(metro_mock.register.call_args[0][0].size, m.equal_to(10))
        m.assert_that(metro_mock.register.call_args[0][0].value['instance'], m.has_length(10))
        m.assert_that(metro_mock.register.call_args[0][1], m.has_length(1))
        metro_factory_mock.assert_called_once_with(complexity_mock)

    @mock.patch('almetro.metro.Metro.new')
    def test_should_measure_algorithm_using_custom_setup(self, metro_factory_mock):
        algorithm_mock = mock.MagicMock()
        complexity_mock = mock.MagicMock()
        metro_mock = mock.MagicMock()
        metro_factory_mock.return_value = metro_mock

        def my_gen():
            for i in range(3):
                yield {'name': 'instance_name', 'size': 3, 'value': {'instance': range(3)}}

        metro = Al()\
            .with_instances(instances=3, provider=generator(my_gen()))\
            .with_execution(trials=2, runs=3)\
            .metro(algorithm_mock, complexity_mock)

        m.assert_that(metro, m.equal_to(metro_mock))
        m.assert_that(algorithm_mock.mock_calls, m.has_length(18))

        for _, _, kargs in algorithm_mock.mock_calls:
            m.assert_that(kargs['instance'], m.equal_to(range(3)))

        m.assert_that(metro_mock.register.mock_calls, m.has_length(3))
        for _, args, _ in metro_mock.register.mock_calls:
            m.assert_that(args[0].size, m.equal_to(3))
            m.assert_that(args[0].value['instance'], m.equal_to(range(3)))
            m.assert_that(args[1], m.has_length(2))

        metro_factory_mock.assert_called_once_with(complexity_mock)
