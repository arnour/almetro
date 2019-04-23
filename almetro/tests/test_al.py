"""
Al test.

"""
from hamcrest import (
    assert_that,
    has_length,
    equal_to,
)
from unittest.mock import MagicMock, patch, ANY
from almetro.al import InstanceSettings, ExecutionSettings, Al
from almetro.instance import InstanceProvider

def test_should_create_al_instance_settings_with_default():
    instance = InstanceSettings()
    assert_that(instance.instances, equal_to(1))
    assert_that(instance.provider, InstanceProvider.new())

def test_should_create_al_instance_settings():
    provider = InstanceProvider.function(lambda x: x*8)
    instance = InstanceSettings(instances=5, provider=provider)
    assert_that(instance.instances, equal_to(5))
    assert_that(instance.provider, provider)

def test_should_create_al_execution_settings_with_default():
    execution = ExecutionSettings()
    assert_that(execution.trials, equal_to(1))
    assert_that(execution.runs, equal_to(1))

def test_should_create_al_execution_settings():
    execution = ExecutionSettings(trials=5, runs=34)
    assert_that(execution.trials, equal_to(5))
    assert_that(execution.runs, equal_to(34))

@patch('almetro.metro.Metro.new')
def test_should_measure_algorithm_using_default_setup(metro_factory_mock):
    algorithm_mock = MagicMock()
    metro_mock = MagicMock()    
    metro_factory_mock.return_value = metro_mock

    metro = Al().metro(algorithm_mock)

    assert_that(metro, equal_to(metro_mock))
    algorithm_mock.assert_called_once_with(range(10))
    metro_mock.register.assert_called_once()
    assert_that(metro_mock.register.call_args[0][0], equal_to(range(10)))
    assert_that(metro_mock.register.call_args[0][1], has_length(1))
    
@patch('almetro.metro.Metro.new')
def test_should_measure_algorithm_using_custom_setup_arnou3(metro_factory_mock):
    algorithm_mock = MagicMock()
    metro_mock = MagicMock()    
    metro_factory_mock.return_value = metro_mock

    metro = Al()\
            .with_instances(instances=3, provider=InstanceProvider.function(lambda : range(2)))\
            .with_execution(trials=2, runs=3)\
            .metro(algorithm_mock)

    assert_that(metro, equal_to(metro_mock))
    assert_that(algorithm_mock.mock_calls, has_length(18))
    for _, args, _ in algorithm_mock.mock_calls:
        assert_that(args[0], equal_to(range(2)))

    assert_that(metro_mock.register.mock_calls, has_length(3))
    for _, args, _ in metro_mock.register.mock_calls:
        assert_that(args[0], equal_to(range(2)))
        assert_that(args[1], has_length(2))
