"""
Al test.

"""
from almetro.tests import TestBase, mock, matchers as m
from almetro.al import InstanceSettings, ExecutionSettings, Al
from almetro.instance import singleton, function


class TestAl(TestBase):

    def test_should_create_al_instance_settings_with_default(self):
        instance = InstanceSettings()
        m.assert_that(instance.instances, m.equal_to(1))
        m.assert_that(instance.provider, singleton(10))

    def test_should_create_al_instance_settings(self):
        provider = function(lambda x: x * 8)
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
        algorithm_mock.assert_called_once_with(range(10))
        metro_mock.register.assert_called_once()
        m.assert_that(metro_mock.register.call_args[0][0], m.equal_to(range(10)))
        m.assert_that(metro_mock.register.call_args[0][1], m.has_length(1))
        metro_factory_mock.assert_called_once_with(complexity_mock)

    @mock.patch('almetro.metro.Metro.new')
    def test_should_measure_algorithm_using_custom_setup(self, metro_factory_mock):
        algorithm_mock = mock.MagicMock()
        complexity_mock = mock.MagicMock()
        metro_mock = mock.MagicMock()
        metro_factory_mock.return_value = metro_mock

        metro = Al()\
            .with_instances(instances=3, provider=function(lambda: range(2)))\
            .with_execution(trials=2, runs=3)\
            .metro(algorithm_mock, complexity_mock)

        m.assert_that(metro, m.equal_to(metro_mock))
        m.assert_that(algorithm_mock.mock_calls, m.has_length(18))
        for _, args, _ in algorithm_mock.mock_calls:
            m.assert_that(args[0], m.equal_to(range(2)))

        m.assert_that(metro_mock.register.mock_calls, m.has_length(3))
        for _, args, _ in metro_mock.register.mock_calls:
            m.assert_that(args[0], m.equal_to(range(2)))
            m.assert_that(args[1], m.has_length(2))

        metro_factory_mock.assert_called_once_with(complexity_mock)
