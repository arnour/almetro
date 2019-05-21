"""
InstanceProvider test.

"""
import random
from almetro.tests import TestBase, matchers as m
from almetro.instance import InstanceProvider, GrowingNumberSequenceProvider
from almetro.instance import growing, function, singleton


class TestInstance(TestBase):

    def test_should_return_randomic_arrays(self):
        provider = InstanceProvider(fn=lambda: random.sample(range(5), 5))

        m.assert_that(provider.new_instance(), m.has_length(5))
        m.assert_that(provider.new_instance(), m.has_length(5))

    def test_should_return_same_instance(self):
        provider = InstanceProvider(fn=lambda: [1, 2, 6])

        m.assert_that(provider.new_instance(), m.has_items(1, 2, 6))
        m.assert_that(provider.new_instance(), m.has_items(1, 2, 6))

    def test_should_return_function_provider(self):
        provider = function(lambda: [1, 5])
        m.assert_that(provider, m.instance_of(InstanceProvider))
        m.assert_that(provider.new_instance(), m.has_length(2))
        m.assert_that(provider.new_instance(), m.has_items(1, 5))

    def test_should_return_growing_provider(self):
        provider = growing(initial_size=1, growth_rate=1.0)
        m.assert_that(provider, m.instance_of(GrowingNumberSequenceProvider))
        m.assert_that(provider.new_instance(), m.has_length(1))
        m.assert_that(provider.new_instance(), m.has_length(2))
        m.assert_that(provider.new_instance(), m.has_length(3))

    def test_should_return_singleton_provider(self):
        provider = singleton(size=4)
        m.assert_that(provider, m.instance_of(InstanceProvider))
        m.assert_that(provider.new_instance(), m.all_of(m.has_length(4), m.equal_to(range(4))))
        m.assert_that(provider.new_instance(), m.all_of(m.has_length(4), m.equal_to(range(4))))
        m.assert_that(provider.new_instance(), m.all_of(m.has_length(4), m.equal_to(range(4))))
