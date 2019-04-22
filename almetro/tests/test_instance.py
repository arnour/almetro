"""
InstanceProvider test.

"""
from hamcrest import (
    assert_that,
    instance_of,
    has_length,
    has_items,
    matches_regexp,
    is_not,
    equal_to,
)
import numpy as np
from almetro.instance import InstanceProvider, GrowingNumberSequenceProvider


def test_should_return_randomic_arrays():
    provider = InstanceProvider(fn=lambda : np.random.random(5))

    assert_that(provider.new(), has_length(5))
    assert_that(provider.new(), has_length(5))

def test_should_return_same_instance():
    provider = InstanceProvider(fn=lambda : np.array([1,2,6]))

    np.testing.assert_array_equal(provider.new(), np.array([1,2,6]))
    np.testing.assert_array_equal(provider.new(), np.array([1,2,6]))


def test_should_return_function_provider():
    provider = InstanceProvider.function(lambda : np.array([1,5]))
    assert_that(provider, instance_of(InstanceProvider))
    assert_that(provider.new(), has_length(2))
    assert_that(provider.new(), has_items(1, 5))

def test_should_return_growing_provider():
    provider = InstanceProvider.growing(size=1, growth_rate=1.0)
    assert_that(provider, instance_of(GrowingNumberSequenceProvider))
    assert_that(provider.new(), has_length(1))
    assert_that(provider.new(), has_length(2))
    assert_that(provider.new(), has_length(3))